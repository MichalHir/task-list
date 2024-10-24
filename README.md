Task list excercise:page 82...
Build a new tasks django rest framework application. Backend only:
    Create task class that has: task name, task deadline date, done(t/F)
    Create api endpoint “/” to show all tasks JSON (urls, serializer, etc.)
    You can use chatgpt
    Use local sqlite database
Add User model:
    Add user model. Add users and add some tasks
    Add endpoint to see specific user tasks
    Add endpoint to add a task
    Add front end 


# My Tennis Club Django Project
https://github.com/ranerlich7/my_tennis_club_django101
https://github.com/ranerlich7/my_shop_django_api

https://github.com/ranerlich7/task_manager

## Setup environment

<!-- 1. **Create and activate a virtual environment:**
    - python -m venv venv
    - source venv\Scripts\activate
    - pip install -r requirements.txt
2. Create the database and superuser
    - python manage.py migrate
    - python manage.py createsuperuser

4. run the server
    - python manage.py runserver

5. add some products in admin or shell and navigate to 'http://127.0.0.1:8000/products/' -->


Setup environment
Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate

pip freeze > requirements.txt
pip install -r requirements.txt

Create the database and superuser
python manage.py makemigrations ...
python manage.py migrate
python manage.py createsuperuser

run the server
python manage.py runserver
Python manage.py shell

add some products in admin or shell and navigate to 'http://127.0.0.1:8000/products/'

michal
michal@gmail.com
1234

create a new repository on the command line:
echo "# task-list" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MichalHir/task-list.git
git push -u origin main

push an existing repository from the command line:
git remote add origin https://github.com/MichalHir/task-list.git
git branch -M main
git push -u origin main