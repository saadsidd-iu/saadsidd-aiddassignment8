from flask import Flask, render_template_string, request, redirect, url_for, flash, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length
import os
from DAL import dal

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this to a random secret key

class ContactForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Send Message')

class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired(), Length(min=2, max=200)])
    description = TextAreaField('Project Description', validators=[DataRequired(), Length(min=10, max=2000)])
    image_filename = SelectField('Project Image', validators=[DataRequired()])
    submit = SubmitField('Add Project')
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # Populate image choices from available images
        available_images = dal.get_available_images()
        self.image_filename.choices = [(img, img) for img in available_images]

# Base HTML Template with CSS link
BASE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+Pro:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <header class="header">
        <div class="container">
            <h1 class="logo">
                <a href="/">Saad Siddique</a>
            </h1>
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="/" class="nav-link">Home</a></li>
                    <li><a href="/about" class="nav-link">About Me</a></li>
                    <li><a href="/resume" class="nav-link">Resume</a></li>
                    <li><a href="/projects" class="nav-link">Projects</a></li>
                    <li><a href="/contact" class="nav-link">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="main">
        <!-- Flash Messages -->
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <div class="flash-messages">
                    {% for category, message in messages %}
                        <div class="flash flash-{{ category }}">{{ message }}</div>
                    {% endfor %}
                </div>
            {% endif %}
        {% endwith %}

        {{ content | safe }}
    </main>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 Saad Siddique. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    content = """
    <section class="hero">
        <div class="container">
            <h1>Welcome to My Digital Space</h1>
            <p>I'm Saad Siddique, a passionate professional dedicated to excellence in technology and innovation. This website serves as my digital resume and portfolio, showcasing my journey, skills, and achievements.</p>
        </div>
    </section>

    <section class="content-section">
        <div class="container">
            <h2>About This Site</h2>
            <div class="grid grid-2">
                <div class="card">
                    <h3>Professional Profile</h3>
                    <p>Explore my professional background, education, and career journey. Learn about my expertise and the value I bring to every project.</p>
                    <a href="/about" class="btn">Learn More</a>
                </div>
                <div class="card">
                    <h3>Resume & Experience</h3>
                    <p>View my detailed resume with comprehensive information about my education, work experience, skills, and professional achievements.</p>
                    <a href="/resume" class="btn">View Resume</a>
                </div>
                <div class="card">
                    <h3>Projects & Portfolio</h3>
                    <p>Discover the projects I've worked on, including detailed descriptions, technologies used, and links to live demonstrations.</p>
                    <a href="/projects" class="btn">View Projects</a>
                </div>
                <div class="card">
                    <h3>Get In Touch</h3>
                    <p>Ready to connect? Reach out through my contact form or connect with me on professional networks. I'm always open to new opportunities.</p>
                    <a href="/contact" class="btn">Contact Me</a>
                </div>
            </div>
        </div>
    </section>

    <section class="content-section">
        <div class="container">
            <h2>Quick Highlights</h2>
            <div class="grid grid-3">
                <div class="card">
                    <h3>Technical Expertise</h3>
                    <p>Proficient in modern technologies and frameworks, with a focus on creating efficient and scalable solutions.</p>
                </div>
                <div class="card">
                    <h3>Problem Solving</h3>
                    <p>Analytical thinker with a proven track record of identifying challenges and implementing effective solutions.</p>
                </div>
                <div class="card">
                    <h3>Continuous Learning</h3>
                    <p>Committed to staying current with industry trends and continuously expanding my skill set.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="content-section">
        <div class="container">
            <h2>Source Code & Repository</h2>
            <div class="github-section">
                <p>This website is built with HTML, CSS, and JavaScript and features responsive design, PDF viewers, and modern web technologies. The complete source code is available on GitHub for review and collaboration.</p>
                <div class="github-link">
                    <a href="https://github.com/saadsidd-iu/AiDD-assignment-7-saad-siddique" target="_blank" class="btn btn-github">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="margin-right: 8px;">
                            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                        </svg>
                        View Source Code on GitHub
                    </a>
                </div>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE_TEMPLATE, title="Home - Saad Siddique", content=content)

@app.route('/about')
def about():
    content = """
    <section class="content-section">
        <div class="container">
            <h1>About Me</h1>
            
            <div class="profile-section">
                <img src="/static/images/profile.jpg" alt="Saad Siddique professional headshot" class="profile-image">
                
                <div class="bio-content">
                    <h2>Professional Background</h2>
                    <p>I am Saad Siddique, a dedicated professional with a passion for technology and innovation. My career has been driven by a commitment to excellence and a desire to make meaningful contributions in the consulting industry.</p>
                    
                    <p>With a strong foundation in both technical and analytical skills, I have developed expertise in various areas of technology and business. My approach combines technical proficiency with strategic thinking, enabling me to deliver solutions that not only meet immediate needs but also contribute to long-term success.</p>
                    
                    <h2>Education & Foundation</h2>
                    <p>My educational background has provided me with a solid foundation in both technical and analytical disciplines. I believe in the power of continuous learning and stay current with the latest industry trends and technologies.</p>
                    
                    <h2>Professional Interests</h2>
                    <p>I am particularly interested in areas where technology intersects with business strategy, data analysis, and user experience. My goal is to leverage technology to solve real-world problems and create value for organizations and individuals alike.</p>
                    
                    <h2>Career Goals</h2>
                    <p>Looking forward, I am committed to advancing my career in technology while contributing to meaningful projects. I am particularly interested in roles that allow me to combine technical expertise with strategic thinking and team collaboration.</p>
                    
                    <h2>Personal Interests</h2>
                    <p>Beyond my professional pursuits, I enjoy staying active in the community, exploring new technologies, and playing recreational soccer. I believe in the importance of work-life balance and enjoy various hobbies that keep me engaged and motivated.</p>
                </div>
            </div>
            
            <div class="skills-section">
                <h2>Core Competencies</h2>
                <div class="grid grid-3">
                    <div class="card">
                        <h3>Technical Skills</h3>
                        <ul>
                            <li>Excel & Access</li>
                            <li>Data Analysis & Visualization</li>
                            <li>HTML/CSS, Python, SQL</li>
                            <li>IT Strategy</li>
                        </ul>
                    </div>
                    <div class="card">
                        <h3>Professional Skills</h3>
                        <ul>
                            <li>Project Management</li>
                            <li>Team Collaboration</li>
                            <li>Problem Solving</li>
                            <li>Strategic Planning</li>
                        </ul>
                    </div>
                    <div class="card">
                        <h3>Soft Skills</h3>
                        <ul>
                            <li>Communication</li>
                            <li>Leadership</li>
                            <li>Adaptability</li>
                            <li>Continuous Learning</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE_TEMPLATE, title="About Me - Saad Siddique", content=content)

@app.route('/projects')
def projects():
    # Get all projects from database
    projects_data = dal.get_all_projects()
    
    # Build projects HTML
    projects_html = ""
    for project in projects_data:
        project_id, title, description, image_filename, created_date, updated_date = project
        
        projects_html += f"""
        <div class="project-card">
            <div class="project-image">
                <img src="/static/images/{image_filename}" alt="{title}" class="project-img">
            </div>
            <div class="project-content">
                <h3>{title}</h3>
                <p class="project-description">{description}</p>
                <div class="project-meta">
                    <small>Created: {created_date}</small>
                </div>
            </div>
        </div>
        """
    
    content = f"""
    <section class="content-section">
        <div class="container">
            <h1>Projects & Portfolio</h1>
            <p>Here are some of the key projects I've worked on, showcasing my technical skills and problem-solving abilities.</p>
            
            <div class="projects-grid">
                {projects_html}
            </div>
            
            <div class="add-project-section">
                <h2>Add New Project</h2>
                <p>Want to add a new project? <a href="/add-project" class="btn">Add Project</a></p>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE_TEMPLATE, title="Projects - Saad Siddique", content=content)

@app.route('/resume')
def resume():
    content = """
    <section class="content-section">
        <div class="container">
            <h1>Resume</h1>
            
            <div class="resume-header">
                <h2>Saad Siddique</h2>
                <p>Professional Summary: Dedicated technology professional with expertise in software development, data analysis, and project management. Committed to delivering innovative solutions and driving organizational success through technical excellence and strategic thinking.</p>
            </div>

            <!-- PDF Viewer Section -->
            <div class="pdf-viewer-section">
                <h3>Resume Document</h3>
                <div class="pdf-container">
                    <iframe 
                        src="/static/Siddique_Saad_Resume.pdf#toolbar=1&navpanes=1&scrollbar=1" 
                        width="100%" 
                        height="800px"
                        title="Saad Siddique Resume PDF"
                        class="pdf-viewer">
                        <p>Your browser does not support PDFs. <a href="/static/Siddique_Saad_Resume.pdf" target="_blank">Click here to download the PDF</a>.</p>
                    </iframe>
                </div>
                
                <div class="pdf-actions">
                    <a href="/static/Siddique_Saad_Resume.pdf" class="btn" target="_blank">Download PDF Resume</a>
                    <a href="/contact" class="btn btn-secondary">Contact Me</a>
                </div>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE_TEMPLATE, title="Resume - Saad Siddique", content=content)

@app.route('/add-project', methods=['GET', 'POST'])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        # Add project to database
        project_id = dal.add_project(
            form.title.data,
            form.description.data,
            form.image_filename.data
        )
        
        if project_id:
            flash('Project added successfully!', 'success')
            return redirect(url_for('projects'))
        else:
            flash('Error adding project. Please try again.', 'error')
    
    content = f"""
    <section class="content-section">
        <div class="container">
            <h1>Add New Project</h1>
            <p>Fill out the form below to add a new project to your portfolio.</p>
            
            <div class="project-form-section">
                <form method="POST" class="project-form" novalidate>
                    {form.hidden_tag()}
                    
                    <div class="form-group">
                        {form.title.label(class_="form-label")}
                        {form.title(class_="form-control", placeholder="Enter project title")}
                        <div class="error-message" style="display: none;">
                            Please enter a project title (minimum 2 characters)
                        </div>
                    </div>

                    <div class="form-group">
                        {form.description.label(class_="form-label")}
                        {form.description(class_="form-control", rows="6", placeholder="Enter project description...")}
                        <div class="error-message" style="display: none;">
                            Please enter a project description (minimum 10 characters)
                        </div>
                    </div>

                    <div class="form-group">
                        {form.image_filename.label(class_="form-label")}
                        {form.image_filename(class_="form-control")}
                        <div class="form-help">
                            <p>Select an image from your static/images folder. To add new images, simply drag and drop them into the static/images folder and refresh this page.</p>
                        </div>
                    </div>

                    <div class="form-group">
                        {form.submit(class_="btn")}
                        <a href="/projects" class="btn btn-secondary">Cancel</a>
                    </div>
                </form>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE_TEMPLATE, title="Add Project - Saad Siddique", content=content)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Here you would typically save the form data to a database
        # For now, we'll just flash a success message
        flash('Thank you for your message! I will get back to you as soon as possible.', 'success')
        return redirect(url_for('thank_you'))
    
    content = f"""
    <section class="content-section">
        <div class="container">
            <h1>Get In Touch</h1>
            <p>I'm always interested in new opportunities and collaborations. Feel free to reach out through any of the channels below or use the contact form.</p>

            <div class="contact-info">
                <div class="contact-item">
                    <h3>Email</h3>
                    <p><a href="mailto:saad.siddique@email.com">saad.siddique@email.com</a></p>
                    <p>I typically respond within 24 hours</p>
                </div>
                
                <div class="contact-item">
                    <h3>LinkedIn</h3>
                    <p><a href="https://www.linkedin.com/in/saadhsiddique/" target="_blank">linkedin.com/in/saadhsiddique</a></p>
                    <p>Connect with me professionally</p>
                </div>
                
                <div class="contact-item">
                    <h3>GitHub</h3>
                    <p><a href="https://github.com/saadsidd-iu/AiDD-assignment-7-saad-siddique" target="_blank">github.com/saadsidd-iu/AiDD-assignment-7-saad-siddique</a></p>
                    <p>View my code and projects</p>
                </div>
            </div>

            <div class="contact-form-section">
                <h2>Send Me a Message</h2>
                <p>Use the form below to send me a direct message. All fields are required.</p>
                
                <form method="POST" class="contact-form" novalidate>
                    {form.hidden_tag()}
                    
                    <div class="form-group">
                        {form.first_name.label(class_="form-label")}
                        {form.first_name(class_="form-control")}
                        <div class="error-message" style="display: none;">
                            Please enter your first name (minimum 2 characters)
                        </div>
                    </div>

                    <div class="form-group">
                        {form.last_name.label(class_="form-label")}
                        {form.last_name(class_="form-control")}
                        <div class="error-message" style="display: none;">
                            Please enter your last name (minimum 2 characters)
                        </div>
                    </div>

                    <div class="form-group">
                        {form.email.label(class_="form-label")}
                        {form.email(class_="form-control")}
                        <div class="error-message" style="display: none;">
                            Please enter a valid email address
                        </div>
                    </div>

                    <div class="form-group">
                        {form.message.label(class_="form-label")}
                        {form.message(class_="form-control", rows="6", placeholder="Please enter your message here...")}
                        <div class="error-message" style="display: none;">
                            Please enter a message (minimum 10 characters)
                        </div>
                    </div>

                    <div class="form-group">
                        {form.submit(class_="btn")}
                    </div>
                </form>
            </div>

            <div class="additional-info">
                <h2>What to Expect</h2>
                <div class="grid grid-2">
                    <div class="card">
                        <h3>Response Time</h3>
                        <p>I typically respond to all inquiries within 24 hours during business days. For urgent matters, please mention it in your message.</p>
                    </div>
                    
                    <div class="card">
                        <h3>Types of Inquiries</h3>
                        <p>I'm open to discussing job opportunities, freelance projects, collaboration ideas, technical questions, and general networking.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE_TEMPLATE, title="Contact - Saad Siddique", content=content)

@app.route('/thank-you')
def thank_you():
    content = """
    <section class="content-section">
        <div class="container">
            <div class="thank-you-content">
                <h1>Thank You!</h1>
                <p class="thank-you-message">Your message has been successfully sent. I appreciate you taking the time to reach out and will get back to you as soon as possible.</p>
                
                <div class="thank-you-actions">
                    <a href="/" class="btn">Back to Homepage</a>
                </div>
            </div>
        </div>
    </section>
    """
    return render_template_string(BASE_TEMPLATE, title="Thank You - Saad Siddique", content=content)

# Route to serve static files (PDFs, images, etc.)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)