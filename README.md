# BreezeCafe
# Breeze Cafe

A dynamic web application for managing a cafe's menu and customer reviews, built with Django and Dockerized for easy deployment. 
This project showcases backend development skills with Python, Django, SQLite, HTML, CSS, and JavaScript.

## Features
- **Dynamic Menu**: Manage food items (name, description, price, image, category) via the Django admin panel.
- **Tabbed Categories**: Separate "Drink Menu" and "Special Items" with tabbed navigation for each category.
- **Review System**: Customers can add reviews with ratings (1-5 stars) and reply to existing reviews for each food item.
- **Dockerized**: Runs in a container with SQLite as the database for simplicity and portability.
- **Responsive Design**: Frontend styled with custom CSS and FontAwesome icons, featuring a video background.

## Tech Stack
- **Backend**: Python 3.12, Django 4.2+
- **Database**: SQLite (`db.sqlite3`)
- **Frontend**: HTML, CSS (tooplate-wave-cafe.css), JavaScript (jQuery)
- **Containerization**: Docker with Docker Compose
- **Dependencies**: Pillow (image handling)

## Project Structure
breeze_cafe/
├── breeze_cafe/          # Django project settings
├── cafe/                # Main app (models, views, templates)
├── static/              # Static files (CSS, JS, video)
├── media/               # Uploaded files (images)
├── staticfiles/         # Collected static files
├── Dockerfile           # Docker image configuration
├── docker-compose.yml   # Docker Compose setup
├── requirements.txt     # Python dependencies
├── manage.py            # Django management script
└── db.sqlite3           # SQLite database

## Prerequisites
- **Docker**: Version 24.0+ (tested with 28.0.1)
- **Docker Compose**: v2.x (integrated plugin, not standalone `docker-compose`)
- **Git**: For cloning the repository

Contact
For questions or contributions, reach out at abnerogega01@gmail.com

