# Portfolio Website - Assignment 7

A modern, responsive portfolio website built with Flask and SQLite database integration.

## Features

- **Responsive Design**: Modern, mobile-friendly interface
- **Database Integration**: SQLite database with Data Access Layer (DAL)
- **Project Management**: Add, view, and manage portfolio projects
- **PDF Viewers**: Embedded PDF viewers for resume and project documents
- **Contact Form**: Functional contact form with validation
- **Dynamic Content**: Database-driven project display

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with custom DAL
- **Frontend**: HTML5, CSS3, JavaScript
- **Forms**: Flask-WTF with WTForms
- **Styling**: Custom CSS with responsive grid layout

## Project Structure

```
├── app.py                 # Main Flask application
├── DAL.py                 # Data Access Layer for database operations
├── init_database.py       # Database initialization script
├── projects.db            # SQLite database file
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Custom stylesheet
│   ├── images/            # Project images
│   └── *.pdf             # Resume and project documents
└── README.md             # This file
```

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/saadsidd-iu/AiDD-assignment-7-saad-siddique.git
   cd AiDD-assignment-7-saad-siddique
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   python init_database.py
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the website**
   Open your browser and navigate to `http://localhost:5000`

## Database Schema

### Projects Table
- `id` (INTEGER, PRIMARY KEY, AUTOINCREMENT)
- `title` (TEXT, NOT NULL)
- `description` (TEXT, NOT NULL)
- `image_filename` (TEXT, NOT NULL)
- `created_date` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
- `updated_date` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

## Usage

### Adding Projects
1. Navigate to the "Add Project" page
2. Fill in the project details
3. Select an image from the available images in `static/images/`
4. Submit the form

### Managing Images
- Add new images by placing them in the `static/images/` folder
- Supported formats: JPG, PNG, GIF, BMP, WEBP
- Refresh the "Add Project" page to see new images in the dropdown

### Database Operations
The DAL (Data Access Layer) provides methods for:
- `add_project(title, description, image_filename)`
- `get_all_projects()`
- `get_project_by_id(project_id)`
- `update_project(project_id, title, description, image_filename)`
- `delete_project(project_id)`
- `get_available_images()`

## Pages

- **Home** (`/`): Welcome page with overview
- **About** (`/about`): Professional background and skills
- **Resume** (`/resume`): PDF viewer with resume
- **Projects** (`/projects`): Database-driven project portfolio
- **Add Project** (`/add-project`): Form to add new projects
- **Contact** (`/contact`): Contact information and form

## Development

### Database Management
```python
from DAL import dal

# Add a new project
project_id = dal.add_project("Project Title", "Description", "image.jpg")

# Get all projects
projects = dal.get_all_projects()

# Get specific project
project = dal.get_project_by_id(1)
```

### Adding New Features
1. Modify `app.py` for new routes
2. Update `DAL.py` for database operations
3. Add styles to `static/css/style.css`
4. Test thoroughly before committing

## License

This project is part of an academic assignment and is for educational purposes.

## Author

**Saad Siddique**
- GitHub: [@saadsidd-iu](https://github.com/saadsidd-iu)
- Repository: [AiDD-assignment-7-saad-siddique](https://github.com/saadsidd-iu/AiDD-assignment-7-saad-siddique)

## Assignment Details

This project fulfills the requirements for Assignment 7, demonstrating:
- Flask web application development
- SQLite database integration
- Data Access Layer implementation
- Form handling and validation
- Responsive web design
- CRUD operations for project management
