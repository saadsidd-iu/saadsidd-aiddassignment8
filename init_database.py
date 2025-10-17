#!/usr/bin/env python3
"""
Database initialization script
This script creates the database and adds some sample projects
"""

from DAL import dal
import os

def init_sample_data():
    """Initialize the database with sample project data"""
    
    # Check if static/images directory exists
    if not os.path.exists("static/images"):
        print("Creating static/images directory...")
        os.makedirs("static/images")
    
    # Get available images
    available_images = dal.get_available_images()
    print(f"Available images: {available_images}")
    
    # Sample projects data
    sample_projects = [
        {
            "title": "ITS CA1 - Information Technology Systems Project",
            "description": "A comprehensive Information Technology Systems project focusing on system analysis, design, and implementation. This project demonstrates understanding of IT infrastructure, system architecture, and technical problem-solving methodologies.",
            "image_filename": "api-screenshot.jpg" if "api-screenshot.jpg" in available_images else available_images[0] if available_images else "default-project.jpg"
        },
        {
            "title": "Team 20 - Helios Case Study",
            "description": "A collaborative case study project analyzing the Helios case, demonstrating team leadership, strategic analysis, and business problem-solving skills. This project showcases ability to work in teams and tackle complex business challenges.",
            "image_filename": "dashboard-screenshot.jpg" if "dashboard-screenshot.jpg" in available_images else available_images[1] if len(available_images) > 1 else "default-project.jpg"
        },
        {
            "title": "E-commerce Website Development",
            "description": "A full-stack e-commerce website built with modern web technologies, featuring user authentication, product catalog, shopping cart, and payment integration.",
            "image_filename": "ecommerce-screenshot.jpg" if "ecommerce-screenshot.jpg" in available_images else available_images[2] if len(available_images) > 2 else "default-project.jpg"
        },
        {
            "title": "Personal Portfolio Website",
            "description": "A responsive personal portfolio website showcasing professional skills, projects, and achievements. Built with Flask, HTML, CSS, and JavaScript.",
            "image_filename": "website-screenshot.jpg" if "website-screenshot.jpg" in available_images else available_images[3] if len(available_images) > 3 else "default-project.jpg"
        }
    ]
    
    # Add sample projects to database
    for project in sample_projects:
        project_id = dal.add_project(
            project["title"],
            project["description"],
            project["image_filename"]
        )
        if project_id:
            print(f"Added project: {project['title']} (ID: {project_id})")
        else:
            print(f"Failed to add project: {project['title']}")
    
    # Display all projects
    print("\nAll projects in database:")
    projects = dal.get_all_projects()
    for project in projects:
        print(f"ID: {project[0]}, Title: {project[1]}, Image: {project[3]}")

if __name__ == "__main__":
    print("Initializing database with sample data...")
    init_sample_data()
    print("Database initialization complete!")
