<h1 align="center"> GMsys </h1>
<p align="center">
  <a href="https://github.com/harry-hov/GMsys/blob/master/blog/static/images/gmicon.png">
    <img src="https://github.com/harry-hov/GMsys/blob/master/blog/static/images/gmicon.png" align="center" height="150" width="150">
  </a>
  <h4 align="center">An Django based Grievance Portal</h4>
</p>

[![Build Status](https://travis-ci.com/harry-hov/GMsys.svg?branch=master)](https://travis-ci.com/harry-hov/GMsys)
[![django1.10](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://www.djangoproject.com)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/harry-hov)

Online Grievance Management System at Institute level

## Prerequisite

<ul>  
<li> Python 3.6 (or later)
  
  It can be installed from:
  https://www.python.org/downloads/
  
<li> Django 2.0 (or later)
  
  It can be installed using:
  
  `pip install django`
  
  To check the django version, open cmd and type:
  ```
  py
  import django
  django.VERSION
  ```
  
</ul>

## Setting up the Project
<ul>  
<li> Forking the Repository
<li> Cloning
  
  <p> You can clone the repo in your local system using following command : </p> 
  
    `git clone https://github.com/user-name/GMsys.git`
    
  Note: Replace "user-name" with your Github username.
     
<li> Setting Upstream
     
    `git remote add upstream https://github.com/harry-hov/GMsys.git`
    
</ul>

## Running project locally
To run the project,
1. Go to the project directory.
2. Open Command Prompt.
3. `py manage.py runserver`
4. Open "http://localhost:8000" in any browser.

## Keeping the project updated
```
git fetch upstream
git rebase upstream/master
git push -f origin master
```
Note: make sure that "master" is your current branch
