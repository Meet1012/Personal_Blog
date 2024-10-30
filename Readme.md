# 🌐 Django Blog Web App

[![Django](https://img.shields.io/badge/Django-4.0%2B-brightgreen)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

This Django project is a simple blog platform where users can view articles, and admins can create, edit, and delete articles. The project includes basic CRUD functionality and authentication for administrative pages. [Project Link](https://roadmap.sh/projects/personal-blog)

## 📋 Features
- View a list of articles on the homepage
- View details of a specific article
- Admin panel for managing articles
- Create, edit, and delete articles through an admin interface

## 📷 ScreenShots
![Home Page](https://assets.roadmap.sh/guest/blog-guest-pages.png)

## Endpoints

Here is a list of available endpoints in the application:

| Endpoint               | URL                   | Description                          |
|------------------------|-----------------------|--------------------------------------|
| Admin Panel            | `/admin/`             | Django’s default admin interface     |
| Homepage               | `/`                   | Displays a list of articles          |
| Article Details        | `/article/<int:id>`   | Displays details of a specific article |
| Admin Home Page        | `/admin_page/`        | Custom admin dashboard               |
| Edit Article           | `/edit/<int:id>`      | Edit an existing article             |
| Delete Article         | `/delete/<int:id>`    | Delete an existing article           |
| New Article            | `/new/`               | Create a new article                 |

## Project Structure

The main components of the project include:
- `views.py`: Contains the view functions for handling requests and rendering templates.
- `urls.py`: Maps URL paths to corresponding views.
- `templates/`: Holds the HTML templates for the frontend.
- `static/`: Stores static assets such as CSS and JavaScript files.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.6+
- Django 3.0+

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-django-blog.git
   cd your-django-blog

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3. **Run migrations:**
    ```bash
    python manage.py migrate

4. **Run migrations:**
    ```bash
    python manage.py runserver

5. **Access the application:**
    1. Open your browser and navigate to `http://127.0.0.1:8000/` for the main page.
    2. Access the admin panel at `http://127.0.0.1:8000/admin_page/` to manage articles.


## Usage

### Viewing Articles
- Visit the homepage (`http://127.0.0.1:8000/`) to see a list of all available articles.
- Click on any article title to view its full content.

### Managing Articles
To manage articles (create, edit, or delete), use the following pages:

1. **Add a New Article**
   - URL: `/new/`
   - Go to `/new/` to add a new article. You will be prompted to enter a title, date, and content.
   - Click **Publish** to save the new article.

2. **Edit an Article**
   - URL: `/edit/<int:id>`
   - Visit `/edit/<int:id>` where `<int:id>` is the article's unique ID.
   - Make changes to the title, date, or content and click **Update** to save the modifications.

3. **Delete an Article**
   - URL: `/delete/<int:id>`
   - To delete an article, navigate to `/delete/<int:id>` (where `<int:id>` is the article ID).
   - This action will remove the article from the database permanently.

4. **Admin Panel**
   - URL: `/admin/`
   - Log in to the Django admin panel to manage articles and access additional administrative functions.
   - Use the superuser credentials created during setup.

5. **Custom Admin Home Page**
   - URL: `/admin_page/`
   - This is a custom admin dashboard for managing the articles directly within the blog application.

## Error Management
- If there are any issues with form submissions (such as missing required fields), the application will display error messages next to each field.
- Ensure all fields are completed before submitting forms on the `/new/` and `/edit/<int:id>` pages.

## API Endpoints (Optional)

If you want to extend this project with RESTful API endpoints, consider using Django REST Framework (DRF). This would enable:
- Programmatic access to articles via endpoints like `/api/articles/`
- CRUD operations for articles through an API client.

### Common Issues

- **Error: `Page Not Found (404)`**
  - Ensure the URL entered is correct and matches the patterns in `urls.py`.
  
- **Error: `CSRF token missing or incorrect`**
  - Make sure you’ve included `{% csrf_token %}` in your form templates when making POST requests.

- **Error: `ValueError at /new/`**
  - Check that all form fields are correctly filled out and meet validation requirements.

