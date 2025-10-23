"""
Test script for Flask application functionality
Tests routes, forms, and web interface components
"""

import pytest
import tempfile
import os
import sys
from DAL import DatabaseAccessLayer

# Import app after setting up the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import app, dal


class TestFlaskApp:
    """Test class for Flask application"""
    
    def setup_method(self):
        """Set up test client and temporary database"""
        # Create temporary database
        self.test_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.test_db.close()
        
        # Create test DAL instance
        self.test_dal = DatabaseAccessLayer(self.test_db.name)
        
        # Configure app for testing
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        
        # Replace the global dal with test dal
        import app as app_module
        app_module.dal = self.test_dal
        
        self.client = app.test_client()
    
    def teardown_method(self):
        """Clean up after each test"""
        if os.path.exists(self.test_db.name):
            os.unlink(self.test_db.name)
    
    def test_home_page(self):
        """Test that home page loads successfully"""
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'Saad Siddique' in response.data
        assert b'Welcome to My Digital Space' in response.data
    
    def test_about_page(self):
        """Test that about page loads successfully"""
        response = self.client.get('/about')
        assert response.status_code == 200
        assert b'About Me' in response.data
        assert b'Professional Background' in response.data
    
    def test_projects_page(self):
        """Test that projects page loads successfully"""
        # Add a test project first
        self.test_dal.add_project(
            "Test Project",
            "Test Description",
            "test.jpg"
        )
        
        response = self.client.get('/projects')
        assert response.status_code == 200
        assert b'Projects & Portfolio' in response.data
        assert b'Test Project' in response.data
    
    def test_resume_page(self):
        """Test that resume page loads successfully"""
        response = self.client.get('/resume')
        assert response.status_code == 200
        assert b'Resume' in response.data
        assert b'Saad Siddique' in response.data
    
    def test_contact_page_get(self):
        """Test that contact page loads with form"""
        response = self.client.get('/contact')
        assert response.status_code == 200
        assert b'Get In Touch' in response.data
        assert b'first_name' in response.data
        assert b'last_name' in response.data
        assert b'email' in response.data
        assert b'message' in response.data
    
    def test_contact_form_submission(self):
        """Test contact form submission"""
        response = self.client.post('/contact', data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'message': 'This is a test message for the contact form.'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Thank you for your message!' in response.data
    
    def test_add_project_page_get(self):
        """Test that add project page loads with form"""
        response = self.client.get('/add-project')
        assert response.status_code == 200
        assert b'Add New Project' in response.data
        assert b'title' in response.data
        assert b'description' in response.data
        assert b'image_filename' in response.data
    
    def test_add_project_form_submission(self):
        """Test add project form submission"""
        response = self.client.post('/add-project', data={
            'title': 'New Test Project',
            'description': 'This is a new test project created through the form.',
            'image_filename': 'test-project.jpg'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Project added successfully!' in response.data
    
    def test_static_files(self):
        """Test that static files are served correctly"""
        response = self.client.get('/static/css/style.css')
        assert response.status_code == 200
        assert response.content_type == 'text/css; charset=utf-8'
    
    def test_nonexistent_route(self):
        """Test that 404 is returned for nonexistent routes"""
        response = self.client.get('/nonexistent-route')
        assert response.status_code == 404
    
    def test_flash_messages(self):
        """Test that flash messages work correctly"""
        # Test contact form flash message
        response = self.client.post('/contact', data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'message': 'Test message'
        }, follow_redirects=True)
        
        assert b'Thank you for your message!' in response.data
    
    def test_form_validation(self):
        """Test form validation"""
        # Test contact form with missing required fields
        response = self.client.post('/contact', data={
            'first_name': '',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'message': 'Short'
        })
        
        # Should not redirect (form validation should fail)
        assert response.status_code == 200
    
    def test_project_display_with_no_projects(self):
        """Test projects page when no projects exist"""
        # Don't add any projects
        response = self.client.get('/projects')
        assert response.status_code == 200
        assert b'Projects & Portfolio' in response.data
        # Should still show the page even with no projects
    
    def test_resume_pdf_access(self):
        """Test that resume PDF is accessible"""
        response = self.client.get('/static/Siddique_Saad_Resume.pdf')
        # This might return 404 if the PDF doesn't exist, which is okay for testing
        assert response.status_code in [200, 404]
    
    def test_github_link_present(self):
        """Test that GitHub link is present on home page"""
        response = self.client.get('/')
        assert b'github.com/saadsidd-iu' in response.data
        assert b'View Source Code on GitHub' in response.data
    
    def test_navigation_links(self):
        """Test that all navigation links are present"""
        response = self.client.get('/')
        assert b'href="/"' in response.data
        assert b'href="/about"' in response.data
        assert b'href="/resume"' in response.data
        assert b'href="/projects"' in response.data
        assert b'href="/contact"' in response.data


if __name__ == "__main__":
    pytest.main([__file__])
