# Django CRUD Application with PostgreSQL

simple **CRUD** (Create, Read, Update, Delete) application built with **Django** and a **PostgreSQL** database.

## Features
- **Create**: Add new records.
- **Read**: View records.
- **Update**: Modify existing records.
- **Delete**: Remove records.

## Requirements
- Python >= 3.8
- Django 5.1.2
- PostgreSQL
- psycopg2 (PostgreSQL adapter)

## Setup

1. **Clone the repo**:

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows: `.\venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure PostgreSQL**: Update `DATABASES` in `settings.py` with your PostgreSQL credentials.

6. **Run migrations**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Run the server**:

    ```bash
    python manage.py runserver
    ```

8. Access the app at (http://127.0.0.1:8000).


