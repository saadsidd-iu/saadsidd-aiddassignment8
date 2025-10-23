# Saad Siddique - Portfolio Website

A professional Flask-based portfolio website showcasing projects, skills, and experience. This project demonstrates modern web development practices with Docker containerization, automated testing, and CI/CD integration.

## 🚀 Live Demo

The website is containerized and can be run locally or deployed to any Docker-compatible platform.

## ✨ Features

- **Responsive Design**: Modern, mobile-friendly interface
- **Database-Driven**: SQLite database for dynamic project management
- **Docker Support**: Fully containerized for easy deployment
- **Automated Testing**: Comprehensive test suite with GitHub Actions
- **Form Handling**: Contact form with validation
- **PDF Integration**: Resume viewer with PDF support
- **Professional UI**: Clean, modern design with custom CSS

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with custom DAL (Data Access Layer)
- **Frontend**: HTML5, CSS3, JavaScript
- **Forms**: Flask-WTF with WTForms
- **Containerization**: Docker & Docker Compose
- **Testing**: pytest with coverage reporting
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
├── app.py                 # Main Flask application
├── DAL.py                 # Database Access Layer
├── init_database.py       # Database initialization script
├── requirements.txt       # Python dependencies
├── test_requirements.txt  # Testing dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── .github/workflows/    # GitHub Actions workflows
├── static/               # Static assets (CSS, images, PDFs)
├── test_*.py            # Test files
└── README.md            # This file
```

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/saadsidd-iu/saadsidd-aiddassignment8.git
   cd saadsidd-aiddassignment8
   ```

2. **Run with Docker Compose**:
   ```bash
   docker-compose up -d
   ```

3. **Access the website**:
   Open http://localhost:5000 in your browser

### Option 2: Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize the database**:
   ```bash
   python init_database.py
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the website**:
   Open http://localhost:5000 in your browser

## 🧪 Testing

The project includes a comprehensive testing suite:

### Run All Tests
```bash
python run_tests.py
```

### Run Specific Test Categories
```bash
# Database tests
python -m pytest test_database.py -v

# Application tests
python -m pytest test_app.py -v

# Integration tests
python -m pytest test_integration.py -v
```

### Run with Coverage
```bash
python -m pytest --cov=. --cov-report=html
```

## 🐳 Docker Management

Use the included management script for easy Docker operations:

```bash
# Windows PowerShell
.\docker-manage.ps1

# Or use Docker commands directly
docker-compose up -d    # Start
docker-compose down     # Stop
docker-compose logs     # View logs
```

## 📊 GitHub Actions

The repository includes automated CI/CD with GitHub Actions:

- **Automated Testing**: Runs on every push and pull request
- **Multi-Version Support**: Tests Python 3.9, 3.10, 3.11
- **Coverage Reporting**: Tracks test coverage over time
- **Artifact Storage**: Saves test reports and coverage data

## 🗄️ Database Schema

The application uses a simple SQLite database with the following schema:

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    image_filename TEXT NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET | `/about` | About page |
| GET | `/projects` | Projects portfolio |
| GET | `/resume` | Resume page |
| GET | `/contact` | Contact form |
| POST | `/contact` | Submit contact form |
| GET | `/add-project` | Add project form |
| POST | `/add-project` | Submit project form |
| GET | `/static/<path>` | Static file serving |

## 🎨 Customization

### Adding New Projects
1. Add images to `static/images/`
2. Use the web form at `/add-project`
3. Or add directly via the database

### Styling
- Main stylesheet: `static/css/style.css`
- Responsive design with CSS Grid and Flexbox
- Custom fonts and color scheme

### Content Updates
- Edit `app.py` for page content
- Update `init_database.py` for sample data
- Modify templates in the route functions

## 🔧 Development

### Prerequisites
- Python 3.9+
- Docker (optional)
- Git

### Setup Development Environment
```bash
# Clone repository
git clone https://github.com/saadsidd-iu/saadsidd-aiddassignment8.git
cd saadsidd-aiddassignment8

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r test_requirements.txt

# Initialize database
python init_database.py

# Run tests
python run_tests.py

# Start development server
python app.py
```

## 📈 Performance

- **Lightweight**: Minimal dependencies
- **Fast Loading**: Optimized static assets
- **Responsive**: Mobile-first design
- **Scalable**: Docker-ready for production

## 🔒 Security

- CSRF protection on forms
- Input validation and sanitization
- Secure file handling
- Environment variable configuration

## 📄 License

This project is part of an academic assignment and is for educational purposes.

## 👨‍💻 Author

**Saad Siddique**
- GitHub: [@saadsidd-iu](https://github.com/saadsidd-iu)
- LinkedIn: [saadhsiddique](https://www.linkedin.com/in/saadhsiddique/)

## 🤝 Contributing

This is an academic project, but suggestions and improvements are welcome!

## 📞 Contact

For questions or collaboration opportunities, please use the contact form on the website or reach out via LinkedIn.

---

**Built with ❤️ using Flask, Docker, and modern web technologies**