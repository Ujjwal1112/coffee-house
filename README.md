# A web Application for Coffee-House
 
## A simple WEB application that sells Coffee to Users
 
A straightforward Python/Django-driven users device management data API, which enables users to perform CRUD(CREATE, READ, UPDATE, DELETE) operations on device data.
 
## Features
 
- Developed using Powerful Django, SQLite and Python
- CRUD operations on products data
- DRF(Django Rest Framework) for API development
- JWT token used for authentication
- Swagger UI for API documentation
 
## Tech
 
- [Python](https://www.python.org/) v3.11
- [Django](https://docs.djangoproject.com/en/4.2/) - Powerful Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Powerful REST API Framework
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Authentication and Authorization
- [SQLite](https://www.sqlite.org/docs.html) - a local database engine
 
 
## Installation
 
This application requires [Python](https://www.python.org/) v3.11 to run.
 
Install the dependencies and devDependencies and start the server.
 
```sh
### Steps to run the project.
 
1. clone the repositiory and open in your favourite terminal
2. cd users-devices-backend
3. run this commnad to install dependencies : pip3 install -r requirements.txt
4. run project : python manage.py runserver
5. open localhost link to browser
6. redirect to /swagger to get swagger view of the project
```
 
 
```sh
### Steps to run the project with docker.
 
1. clone the repositiory and open in your favourite terminal
2. cd users-devices-backend
3. run this commnad to run project in docker container : docker-compose up --build
4. open localhost link to browser
5. redirect to /swagger to get swagger view of the project
```
