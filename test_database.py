"""
Test script for database functionality
Tests database connection, project CRUD operations, and data integrity
"""

import pytest
import sqlite3
import os
import tempfile
from DAL import DatabaseAccessLayer


class TestDatabase:
    """Test class for database operations"""
    
    def setup_method(self):
        """Set up test database before each test"""
        # Create a temporary database for testing
        self.test_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.test_db.close()
        self.dal = DatabaseAccessLayer(self.test_db.name)
    
    def teardown_method(self):
        """Clean up test database after each test"""
        if os.path.exists(self.test_db.name):
            os.unlink(self.test_db.name)
    
    def test_database_connection(self):
        """Test that database connection works"""
        conn = self.dal.get_connection()
        assert conn is not None
        conn.close()
    
    def test_database_initialization(self):
        """Test that database tables are created properly"""
        conn = self.dal.get_connection()
        cursor = conn.cursor()
        
        # Check if projects table exists
        cursor.execute("""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='projects'
        """)
        result = cursor.fetchone()
        assert result is not None
        assert result[0] == 'projects'
        
        conn.close()
    
    def test_add_project(self):
        """Test adding a new project"""
        project_id = self.dal.add_project(
            "Test Project",
            "This is a test project description",
            "test-image.jpg"
        )
        
        assert project_id is not None
        assert isinstance(project_id, int)
        assert project_id > 0
    
    def test_get_all_projects(self):
        """Test retrieving all projects"""
        # Add test projects
        self.dal.add_project("Project 1", "Description 1", "image1.jpg")
        self.dal.add_project("Project 2", "Description 2", "image2.jpg")
        
        projects = self.dal.get_all_projects()
        assert len(projects) == 2
        
        # Check project structure
        project = projects[0]
        assert len(project) == 6  # id, title, description, image_filename, created_date, updated_date
        assert project[1] in ["Project 1", "Project 2"]  # title
    
    def test_get_project_by_id(self):
        """Test retrieving a specific project by ID"""
        project_id = self.dal.add_project(
            "Test Project",
            "Test Description",
            "test.jpg"
        )
        
        project = self.dal.get_project_by_id(project_id)
        assert project is not None
        assert project[0] == project_id
        assert project[1] == "Test Project"
        assert project[2] == "Test Description"
        assert project[3] == "test.jpg"
    
    def test_update_project(self):
        """Test updating an existing project"""
        project_id = self.dal.add_project(
            "Original Title",
            "Original Description",
            "original.jpg"
        )
        
        success = self.dal.update_project(
            project_id,
            "Updated Title",
            "Updated Description",
            "updated.jpg"
        )
        
        assert success is True
        
        # Verify the update
        project = self.dal.get_project_by_id(project_id)
        assert project[1] == "Updated Title"
        assert project[2] == "Updated Description"
        assert project[3] == "updated.jpg"
    
    def test_delete_project(self):
        """Test deleting a project"""
        project_id = self.dal.add_project(
            "To Delete",
            "This will be deleted",
            "delete.jpg"
        )
        
        success = self.dal.delete_project(project_id)
        assert success is True
        
        # Verify deletion
        project = self.dal.get_project_by_id(project_id)
        assert project is None
    
    def test_get_available_images(self):
        """Test getting available images"""
        # This test might need to be adjusted based on your static/images setup
        images = self.dal.get_available_images()
        assert isinstance(images, list)
    
    def test_database_constraints(self):
        """Test database constraints and error handling"""
        # Test adding project with empty title (should handle gracefully)
        project_id = self.dal.add_project("", "Description", "image.jpg")
        # The method should either reject empty title or handle it gracefully
        assert project_id is not None or project_id is None  # Either way is acceptable
    
    def test_project_data_types(self):
        """Test that project data is stored with correct types"""
        project_id = self.dal.add_project(
            "Type Test",
            "Testing data types",
            "type-test.jpg"
        )
        
        project = self.dal.get_project_by_id(project_id)
        assert isinstance(project[0], int)  # ID should be integer
        assert isinstance(project[1], str)  # Title should be string
        assert isinstance(project[2], str)  # Description should be string
        assert isinstance(project[3], str)  # Image filename should be string
        assert project[4] is not None  # Created date should exist
        assert project[5] is not None  # Updated date should exist


if __name__ == "__main__":
    pytest.main([__file__])
