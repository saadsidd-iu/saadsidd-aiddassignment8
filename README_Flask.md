# Saad Siddique Personal Website - Flask Version

This is a Flask web application version of the personal website, converted from the original HTML/CSS/JavaScript implementation.

## Features

- **Responsive Design**: Modern, clean layout that works on all devices
- **Contact Form**: Functional contact form with server-side validation using Flask-WTF
- **PDF Viewers**: Embedded PDF viewers for resume and project documents
- **Template System**: Uses Jinja2 templates for maintainable code structure
- **Static File Serving**: Properly organized static files (CSS, images, PDFs)

## Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # Jinja2 templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Homepage
│   ├── about.html        # About page
│   ├── resume.html       # Resume page
│   ├── projects.html     # Projects page
│   ├── contact.html      # Contact page
│   └── thankyou.html     # Thank you page
└── static/              # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    ├── images/           # Image assets
    └── *.pdf            # PDF documents
```

## Installation & Setup

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Access the Website**:
   Open your browser and go to `http://localhost:5000`

## Features Overview

### Pages
- **Home**: Welcome page with site overview and quick highlights
- **About**: Professional background, skills, and personal information
- **Resume**: PDF viewer with downloadable resume
- **Projects**: Showcase of key projects with embedded PDF documents
- **Contact**: Contact information and functional contact form
- **Thank You**: Confirmation page after form submission

### Contact Form
- Server-side validation using Flask-WTF
- Required fields: First Name, Last Name, Email, Message
- Email format validation
- Message length validation (10-1000 characters)
- Success/error flash messages

### PDF Integration
- Embedded PDF viewers for resume and project documents
- Download links for all PDF files
- Responsive PDF containers

## Customization

### Adding New Pages
1. Create a new template in the `templates/` directory
2. Add a new route in `app.py`
3. Update navigation in `base.html` if needed

### Modifying Content
- Edit the respective template files in `templates/`
- Update static files in the `static/` directory
- Modify the CSS in `static/css/style.css`

### Contact Form Configuration
- Update the `ContactForm` class in `app.py` to modify form fields
- Add email sending functionality by integrating with services like SendGrid or SMTP
- Modify form validation rules as needed

## Deployment

For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up environment variables for configuration
- Using a proper database for contact form submissions
- Implementing email sending functionality
- Adding SSL/HTTPS support

## Dependencies

- **Flask**: Web framework
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation
- **Werkzeug**: WSGI utilities

## Original Website

This Flask application maintains all the functionality and design of the original HTML website while adding:
- Server-side form processing
- Template inheritance for maintainability
- Better organization of static files
- Flask's built-in development server
- Easy extensibility for future features

## License

© 2024 Saad Siddique. All rights reserved.

