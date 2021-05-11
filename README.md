# Shopify Developer Intern Challenge(Fall 2021)

Pikify is a web application that allows its registered users to save images into their personal repository. The users can search for images related to a certain word and are able to save the result of their search onto their repository, one at a time or in bullk.



## Table of Contents
1. [ Entity Relational Diagram](#EntityRelationalDiagram)
2. [ Prototypes](https://github.com/Monica-Uwalaka/pikify/wiki/Prototypes)
3. [ Technology Stack](#TechnologyStack)
4.  [ Setup](#Setup)
5.  [Tests](#Tests)
6.  [ Deployed app](#Deployedapp)
7.  [ Video](#Video)
 
 
 



## 1. <a name='EntityRelationalDiagram'></a> Entity Relational Diagram
![pikify (2)](https://user-images.githubusercontent.com/44309803/117649071-4fd63000-b14c-11eb-866c-cc60d5bd979c.png)


## 3. <a name='TechnologyStack'></a> Technology Stack
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Python](https://www.python.org/)
- [Bootstrap](https://getbootstrap.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [JavaScript](https://www.javascript.com/)
- [Pexels API](https://www.pexels.com/api/documentation/)
- HTML
- CSS

## 4. <a name='Setup'></a> Setup
Assuming you already have postgres installed and a superuser created, first create a postgres database for Pikify's server:
```bash
psql 
CREATE DATABASE pikify_database; # Inside psql shell
```
Clone Pikify's git repository
```bash
https://github.com/Monica-Uwalaka/pikify.git
```

Next, setup a virtual environment and install requirements:
```bash
cd pikify
virtualenv venv --python=python3
source venv/bin/activate # Assuming Linux/MacOS, Venv\Scripts\activate for Windows
cd back-end/api
pip install -r requirements.txt
python manage.py migrate
```
From now on, to run the server from the back-end/api/ directory (ensure your virtualenv is always activated first):
```bash
python manage.py runserver
```
## 5. <a name='Tests'></a> Tests
Pikify has a model and endpoint tests for our back-end. Ensure that your virtualenv to run the back-end is activated before running the below commands.
```bash
cd back-end/api
python manage.py test
```

## 6. <a name='Deployedapp'></a> Deployed app
https://pikify.herokuapp.com/pikify/


## 7. <a name='Video'></a> Video
https://www.youtube.com/watch?v=fuYcnAU1-Pw









