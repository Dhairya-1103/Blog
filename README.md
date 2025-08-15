# Blog 

A simple, production-ready starter blog built with **Django**, featuring posts, tags, comments, search, and auth.

## Features
- Create, edit, delete posts (authors only)
- Comments (authenticated users)
- Tagging + tag pages
- Full-text search (title/body/tags)
- Auth (login/logout) using Django's built-in views
- Bootstrap UI (CDN)

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Project Structure
```
myblog/
  blog/
    templates/blog/
    templates/registration/
  static/
  myblog/
```
## Environment
- Django 4.2
- Python 3.10+
- Timezone: Asia/Kolkata

