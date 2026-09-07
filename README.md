# Rifat Portfolio

Full-stack portfolio built with React, Vite, Django REST Framework, and MySQL-compatible Django models.

## Local development

1. `cd backend && python -m venv .venv && .venv\\Scripts\\activate && pip install -r requirements.txt`
2. Copy `.env.example` to `.env`, then run `python manage.py migrate && python manage.py runserver`
3. `cd frontend && npm install && npm run dev`

Set `VITE_API_URL=http://127.0.0.1:8000/api` in `frontend/.env` when using the Django API.
