
# django-blog

1.Install python 3 ( If your os is not Ubuntu 16.04 )
  - Ubuntu 16.04 ships with both Python 3 and Python 2 pre-installed

2.Setup Virtual Env

# How to install virtualenv:

### Install **pip** first

    sudo apt-get install python3-pip

### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

### Create a folder
    mkdir django-blog
    
### Go to projects folder
    cd django-blog
    
### Create virtualenv using Python3
    virtualenv -p python3 venv

### Active your virtual environment:    
    
    source venv/bin/activate
  
### To deactivate:

    deactivate

### Activate your virtuale environment
      source venv/bin/activate
  
### Install packages and dependencies via pip
      pip install django

## Now Lets Create django project

  ### Create django Project
      django-admin startproject blog
 
 ### Go to blog directory we have created
      cd blog
      
 ### Run project and See
      python manage.py runserver

### Go to browser and copy paste url 
     http://127.0.0.1:8000/
  
  - Congratulations!!If you see The install worked successfully! Congratulations!


