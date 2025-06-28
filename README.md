# Todo Project

A simple Django-based Todo application with a basic frontend for managing tasks. This project demonstrates the use of Django for backend development and includes a minimal frontend for user interaction.

## Features

- Add, view, and manage todo items
- User-friendly web interface
- Uses Django's ORM for database operations
- Organized project structure with templates and static files

## Project Structure

```
todoproject/
├── frontend/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── home/
│           ├── createtodo.html
│           └── home.html
├── media/
├── templates/
│   └── base.html
├── todoproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
├── db.sqlite3
├── manage.py
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- Django (see requirements section)

### Installation

1. Clone the repository:

   ```sh
   git clone <your-repo-url>
   cd todoproject
   ```

2. (Optional) Create and activate a virtual environment:

   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Unix/Mac
   ```

3. Install dependencies:

   ```sh
   pip install django
   ```

4. Apply migrations:

   ```sh
   python manage.py migrate
   ```

5. Run the development server:

   ```sh
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Access the homepage to view and create todo items.
- Use the provided forms to add new tasks.

## Project Organization

- **frontend/**: Django app containing models, views, forms, and templates for the todo functionality.
- **media/**: Directory for user-uploaded files (if any).
- **templates/**: Base templates for the project.
- **todoproject/static/**: Static files (CSS, JS) for styling and interactivity.

## Customization

- Modify `frontend/models.py` to change the todo model.
- Update templates in `frontend/templates/home/` for UI changes.
- Add static files in `todoproject/static/` as needed.

## License

This project is for educational purposes.
