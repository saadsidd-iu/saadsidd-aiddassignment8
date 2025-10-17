import sqlite3
import os
from datetime import datetime

class DatabaseAccessLayer:
    def __init__(self, db_name="projects.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialize the database and create tables if they don't exist"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Create projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                image_filename TEXT NOT NULL,
                created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_connection(self):
        """Get a database connection"""
        return sqlite3.connect(self.db_name)
    
    def add_project(self, title, description, image_filename):
        """Add a new project to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO projects (title, description, image_filename)
                VALUES (?, ?, ?)
            ''', (title, description, image_filename))
            
            conn.commit()
            project_id = cursor.lastrowid
            return project_id
        except Exception as e:
            print(f"Error adding project: {e}")
            return None
        finally:
            conn.close()
    
    def get_all_projects(self):
        """Get all projects from the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                SELECT id, title, description, image_filename, created_date, updated_date
                FROM projects
                ORDER BY created_date DESC
            ''')
            
            projects = cursor.fetchall()
            return projects
        except Exception as e:
            print(f"Error getting projects: {e}")
            return []
        finally:
            conn.close()
    
    def get_project_by_id(self, project_id):
        """Get a specific project by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                SELECT id, title, description, image_filename, created_date, updated_date
                FROM projects
                WHERE id = ?
            ''', (project_id,))
            
            project = cursor.fetchone()
            return project
        except Exception as e:
            print(f"Error getting project: {e}")
            return None
        finally:
            conn.close()
    
    def update_project(self, project_id, title, description, image_filename):
        """Update an existing project"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                UPDATE projects 
                SET title = ?, description = ?, image_filename = ?, updated_date = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (title, description, image_filename, project_id))
            
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating project: {e}")
            return False
        finally:
            conn.close()
    
    def delete_project(self, project_id):
        """Delete a project by ID"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('DELETE FROM projects WHERE id = ?', (project_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting project: {e}")
            return False
        finally:
            conn.close()
    
    def get_available_images(self):
        """Get list of available images in the static/images folder"""
        images_dir = "static/images"
        if not os.path.exists(images_dir):
            return []
        
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
        images = []
        
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(image_extensions):
                images.append(filename)
        
        return sorted(images)

# Create a global instance
dal = DatabaseAccessLayer()
