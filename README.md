# Project Name: DRF Project

## Overview

This project is built using Django Rest Framework (DRF), a powerful and flexible toolkit for building Web APIs with Django. It provides a comprehensive set of features for developing robust, secure, and scalable RESTful APIs.

## Features

- **Easy Serialization:** Convert complex data types like Django models into native Python data types that can be easily rendered into JSON, XML, or other content types.
- **Authentication & Permissions:** Robust built-in mechanisms for handling authentication and permissions.
- **Browsable API:** A web-based interface for interacting with your API, enhancing developer productivity.
- **Viewsets & Routers:** Simplify the creation of CRUD operations with viewsets and routers.
- **Flexible Request Parsing:** Support for multiple request formats.
- **Testing Utilities:** Tools for testing APIs to ensure reliability and correctness.

## Getting Started

### Prerequisites

- Python 3.12.0
- Django 5.0.6
- Django Rest Framework 3.15.1

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/sMmominur/django_rest_framework.git
    cd drf-project
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

### Project Structure

```plaintext
drf-project/
├── core/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── drf_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
