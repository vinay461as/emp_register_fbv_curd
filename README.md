# emp_register_fbv_curd
This is a simple Employee registration project to add, edit and delete the record

# Install Required Packages
The project was built and tested with Django 3.x version.The Django project need some Python package to install
```
pip install Django
pip install django-crispy-forms
```
# Running the Application
Before running the application we need to create the needed DB tables:
```
python manage.py makemigrations
python manage.py migrate
 ```
Now run the server
```
python manage.py runserver
```
To access the applications, go to the URL http://localhost:8000/
