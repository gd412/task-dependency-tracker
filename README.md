Backend system for managing tasks and task dependencies using Django REST Framework.

Tech Stack
Python 3.13
Django, Django REST Framework
MySQL
Git, GitHub

Features
CRUD operations for tasks
Task dependency mapping
Dependency validation before completion
Task status workflow: TODO, IN_PROGRESS, COMPLETED, BLOCKED
Admin panel support

Core Models
Task
title, description
status
created_at, updated_at
TaskDependency

task
depends_on

API Endpoints
GET    /api/tasks/
POST   /api/tasks/
GET    /api/tasks/<id>/
PUT    /api/tasks/<id>/
DELETE /api/tasks/<id>/
POST   /api/dependencies/

Run Locally
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Author: Deepika G
