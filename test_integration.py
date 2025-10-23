"""
Integration test script for the complete Flask website
Tests end-to-end functionality and user workflows
"""

import pytest
import tempfile
import os
import json
from app import app, dal
from DAL import DatabaseAccessLayer


class TestIntegration:
    """Integration tests for the complete website"""
    
    def setup_method(self):
        """Set up test environment"""
        # Create temporary database
        self.test_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.test_db.close()
        
        # Create test DAL instance
        self.test_dal = DatabaseAccessLayer(self.test_db.name)
        
        # Configure app for testing
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        
        # Replace the global dal with test dal
        import app
        app.dal = self.test_dal
        
        self.client = app.test_client()
    
    def teardown_method(self):
        """Clean up after each test"""
        if os.path.exists(self.test_db.name):
            os.unlink(self.test_db.name)
    
    def test_complete_user_journey(self):
        """Test complete user journey through the website"""
        # 1. Visit home page
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'Saad Siddique' in response.data
        
        # 2. Navigate to about page
        response = self.client.get('/about')
        assert response.status_code == 200
        assert b'About Me' in response.data
        
        # 3. Navigate to projects page
        response = self.client.get('/projects')
        assert response.status_code == 200
        assert b'Projects & Portfolio' in response.data
        
        # 4. Navigate to resume page
        response = self.client.get('/resume')
        assert response.status_code == 200
        assert b'Resume' in response.data
        
        # 5. Navigate to contact page
        response = self.client.get('/contact')
        assert response.status_code == 200
        assert b'Get In Touch' in response.data
    
    def test_project_management_workflow(self):
        """Test complete project management workflow"""
        # 1. Check initial projects page (should be empty or have sample data)
        response = self.client.get('/projects')
        assert response.status_code == 200
        
        # 2. Add a new project
        response = self.client.post('/add-project', data={
            'title': 'Integration Test Project',
            'description': 'This project was created during integration testing to verify the complete workflow.',
            'image_filename': 'integration-test.jpg'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Project added successfully!' in response.data
        
        # 3. Verify project appears on projects page
        response = self.client.get('/projects')
        assert response.status_code == 200
        assert b'Integration Test Project' in response.data
        assert b'This project was created during integration testing' in response.data
    
    def test_contact_form_workflow(self):
        """Test complete contact form workflow"""
        # 1. Visit contact page
        response = self.client.get('/contact')
        assert response.status_code == 200
        assert b'Get In Touch' in response.data
        
        # 2. Submit contact form
        response = self.client.post('/contact', data={
            'first_name': 'Integration',
            'last_name': 'Tester',
            'email': 'integration@test.com',
            'message': 'This is an integration test message to verify the contact form workflow works correctly.'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Thank you for your message!' in response.data
        
        # 3. Verify redirect to thank you page
        assert b'Thank You!' in response.data
    
    def test_database_persistence(self):
        """Test that data persists across requests"""
        # 1. Add a project
        project_id = self.test_dal.add_project(
            "Persistence Test Project",
            "Testing data persistence across requests",
            "persistence-test.jpg"
        )
        assert project_id is not None
        
        # 2. Verify project exists in database
        project = self.test_dal.get_project_by_id(project_id)
        assert project is not None
        assert project[1] == "Persistence Test Project"
        
        # 3. Verify project appears on website
        response = self.client.get('/projects')
        assert response.status_code == 200
        assert b'Persistence Test Project' in response.data
    
    def test_error_handling(self):
        """Test error handling across the application"""
        # 1. Test 404 for nonexistent route
        response = self.client.get('/nonexistent-page')
        assert response.status_code == 404
        
        # 2. Test invalid form submission
        response = self.client.post('/contact', data={
            'first_name': '',  # Empty required field
            'last_name': 'Test',
            'email': 'invalid-email',  # Invalid email format
            'message': 'Short'  # Too short message
        })
        assert response.status_code == 200  # Should return form with errors, not crash
    
    def test_static_assets_loading(self):
        """Test that all static assets load correctly"""
        # Test CSS file
        response = self.client.get('/static/css/style.css')
        assert response.status_code == 200
        
        # Test that pages include CSS link
        response = self.client.get('/')
        assert b'<link rel="stylesheet" href="/static/css/style.css">' in response.data
    
    def test_responsive_design_elements(self):
        """Test that responsive design elements are present"""
        response = self.client.get('/')
        
        # Check for viewport meta tag
        assert b'<meta name="viewport"' in response.data
        
        # Check for responsive CSS classes
        assert b'container' in response.data
        assert b'grid' in response.data
    
    def test_seo_elements(self):
        """Test that SEO elements are present"""
        response = self.client.get('/')
        
        # Check for proper HTML structure
        assert b'<!DOCTYPE html>' in response.data
        assert b'<html lang="en">' in response.data
        assert b'<title>' in response.data
        assert b'<meta charset="UTF-8">' in response.data
    
    def test_accessibility_features(self):
        """Test basic accessibility features"""
        response = self.client.get('/')
        
        # Check for alt attributes on images
        assert b'alt=' in response.data
        
        # Check for proper heading structure
        assert b'<h1>' in response.data
        assert b'<h2>' in response.data
        
        # Check for proper form labels
        response = self.client.get('/contact')
        assert b'<label' in response.data
    
    def test_performance_basic(self):
        """Test basic performance requirements"""
        import time
        
        # Test that pages load within reasonable time
        start_time = time.time()
        response = self.client.get('/')
        end_time = time.time()
        
        assert response.status_code == 200
        assert (end_time - start_time) < 5.0  # Should load within 5 seconds
    
    def test_data_integrity(self):
        """Test data integrity across operations"""
        # 1. Add multiple projects
        project_ids = []
        for i in range(3):
            project_id = self.test_dal.add_project(
                f"Test Project {i+1}",
                f"Description for project {i+1}",
                f"image{i+1}.jpg"
            )
            project_ids.append(project_id)
        
        # 2. Verify all projects exist
        projects = self.test_dal.get_all_projects()
        assert len(projects) >= 3
        
        # 3. Verify project data integrity
        for project in projects:
            assert len(project) == 6  # All fields present
            assert project[1] is not None  # Title not null
            assert project[2] is not None  # Description not null
            assert project[3] is not None  # Image filename not null


if __name__ == "__main__":
    pytest.main([__file__])
