# Django E-Learning Platform

A Django-based E-Learning platform for managing courses, subjects, and modules.

## Features

- Course management system
- Subject categorization
- Module organization within courses
- Django Admin interface for content management
- User authentication and authorization

## Project Structure

```
E-Learning/
├── educa/
│   ├── courses/          # Main courses app
│   │   ├── models.py     # Subject, Course, Module models
│   │   ├── admin.py      # Admin configuration
│   │   ├── views.py      # View functions
│   │   └── templates/    # HTML templates
│   ├── educa/            # Project settings
│   │   ├── settings.py   # Django settings
│   │   └── urls.py       # URL configuration
│   └── manage.py         # Django management script
└── README.md
```

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** (Python 3.13 recommended)
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## Setup Instructions

Follow these steps to set up the project on a new computer:

### 1. Clone the Repository

```bash
git clone https://github.com/Kadiwalhussain/E-Learning.git
cd E-Learning
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies:

**On macOS/Linux:**
```bash
python3 -m venv env/educa
source env/educa/bin/activate
```

**On Windows:**
```bash
python -m venv env\educa
env\educa\Scripts\activate
```

### 3. Install Dependencies

Navigate to the project directory and install required packages:

```bash
cd educa
pip install -r ../requirements.txt
```

If `requirements.txt` doesn't exist, install Django directly:

```bash
pip install Django==5.0.14
```

### 4. Run Database Migrations

Create the database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:
- Username
- Email address (optional)
- Password

### 6. Load Initial Data (Optional)

If you have fixture data:

```bash
python manage.py loaddata courses/fixtures/courses.json
```

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Usage

### Accessing the Admin Panel

1. Navigate to http://127.0.0.1:8000/admin/
2. Log in with the superuser credentials you created
3. You can now:
   - Add Subjects
   - Create Courses
   - Add Modules to courses
   - Manage users

### Creating Course Data

1. Log into the admin panel
2. Go to **Subjects** and create a subject (e.g., "Python Programming")
3. Go to **Courses** and create a course:
   - Select an owner (user)
   - Select a subject
   - Enter title, slug, and overview
4. Add modules to the course using the inline form

## Models

### Subject
- `title`: Subject name
- `slug`: URL-friendly identifier

### Course
- `owner`: User who created the course
- `subject`: Subject category
- `title`: Course title
- `slug`: URL-friendly identifier
- `overview`: Course description
- `created`: Creation timestamp

### Module
- `course`: Parent course
- `title`: Module title
- `description`: Module description

## Common Commands

### Database Operations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Data Management
```bash
# Export data to JSON
python manage.py dumpdata courses --indent=2 --output=courses/fixtures/courses.json

# Load data from JSON
python manage.py loaddata courses/fixtures/courses.json
```

### Development
```bash
# Run development server
python manage.py runserver

# Run on specific port
python manage.py runserver 8080

# Check for errors
python manage.py check
```

## Troubleshooting

### ModuleNotFoundError: No module named 'courses'
- Ensure you're in the `educa` directory when running commands
- Verify the app name in `settings.py` matches the directory name

### Database errors
- Run `python manage.py migrate` to apply migrations
- If issues persist, delete `db.sqlite3` and run migrations again

### Port already in use
- Use a different port: `python manage.py runserver 8080`
- Or stop the process using port 8000

## Project Information

- **Django Version**: 5.0.14
- **Python Version**: 3.13 (compatible with 3.8+)
- **Database**: SQLite (default, can be changed in settings)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please open an issue on the GitHub repository.

---

**Happy Learning! 🎓**

