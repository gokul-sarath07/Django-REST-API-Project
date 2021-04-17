# Vernacular.ai Project

### To Run Server, To Create Docker Image and Docker Container
- Type `docker-compose up`
- Docker Image Size: `228.29 MB`
- After build is complete, go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Insights
- Choose an API (Room or Age).
- Select Form Input to input data. (NEXT "ID" IS 9 FOR BOTH)
- Select View Output to view output in API View.
- Note: The database already contains some data. So if you click (Room or Age) output, you can see them in API View.

### Create Super-User
- `python manage.py createsuperuser`
- Note: Current username and passwork is given below.
 - username: gokul
 - passwork: 123qwerty456

### Create Django Project
- `django-admin startproject <PROJECT NAME>`

### Create New App
- `python manage.py startapp <APP NAME>`

### Making Migrations
- `python manage.py makemigrations`
- `python manage.py migrate`




