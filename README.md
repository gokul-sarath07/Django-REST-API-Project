# Vernacular.ai Project

### To Run Server, To Create Docker Image and Docker Container
- Type: `docker-compose up`
- Docker Image Size: `228.29 MB`
- After build is complete, Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to view website.

### Insights
- Choose an API (Room or Age).
- Select Form Input to input data (NEXT "ID" IS `9` FOR BOTH).
- Select View Output to view output in API View.
- Note: The database already contains some data. So if you click (Room or Age) output, you can see them in API View.

### Assumptions Made
- For the first API (Room API), The inputs I collect from the user are an id, values (which consist of id types) and pick_first (boolean value, default=False).
- For the second API (Age API), The inputs I collect from the user are an id, values (which consist of different ages), pick_first (boolean value, default=False) and Constraint value (Boolean value which desides if their is a constraint or not, default=False, which means no constraints).
- I wasn't sure if i needed to add the docker image file, so i didn't add it.
- I wasn't sure if i needed to deploy this project to a server, so i didn't deploy it.

## Commands Used

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




