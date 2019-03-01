# eCommerce

| <a href="https://github.com/DamianMcNulty/ecommerce/stargazers">     <img src="https://img.shields.io/github/stars/DamianMcNulty/ecommerce.svg?style=social" alt="GitHub stars"> </a> | [![Build Status](https://travis-ci.org/DamianMcNulty/ecommerce.svg?branch=master)](https://travis-ci.org/DamianMcNulty/ecommerce) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |

## Goal

> To create an ecommerce app using Django

## Table of Contents

-   [Description](#description)
-   [UX](#ux)
-   [Architecture Diagram](#architecture-diagram)
-   [Technologies Used](#technologies-used)
-   [Development Environment](#development-environment)
-   [Local Testing](#local-testing)
-   [Cross Browser Testing](#cross-browser-testing)
-   [Deployment](#deployment)
-   [Credits](#credits)
-   [LICENSE](#license)

## Description

[(Back to top)](#table-of-contents)

This project is an application for software developers and their users, so users can report problems with an application that they are using and can request new features. Software developers can earn an income from any new feature requests from the users of the application.

## UX

[(Back to top)](#table-of-contents)

### User Stories

A user does not have to pay to use the issue tracker service. 
A user does not have to pay for bug fixes by the developer. 
A user must pay for the developer to develop additional features. 
A user can create a ticket. 
A user can comment on a ticket. 
A user can see the status of the ticket (e.g. ‘to do,’ ‘doing,’ or ‘done’). 
A user can upvote bugs. A user can upvote features. 
A user can upvote bugs for free. 
A user needs to pay to upvote a feature. (with a minimum amount of your choice) to pay for your time in working on it. 
A user can see how many bugs or features are tended to on a daily, weekly and monthly basis 
A user can see the highest-voted bugs and features. 
A user can read a blog. 
A user gains extra perks for active participation. 
A user can read information describing the application. 
A new developer can setup a development environment quickly using the provided documentation.

### Wireframes

see wireframes folder

### Design Demonstration

<img src="https://github.com/DamianMcNulty/ecommerce/blob/master/wireframes/AdobeXDCC.gif" width=30% height=350px alt="Demonstration">

## Architecture diagram

<img src="https://github.com/DamianMcNulty/ecommerce/blob/master/wireframes/ArchitectureDiagram.png" width=100%  alt="Architecture">

## Technologies Used

1.  [HTML5](https://en.wikipedia.org/wiki/HTML5) 

2.  [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)  

3.  [Git](https://git-scm.com/)  

4.  [Github](https://github.com/)

5.  [Online Converter](https://www.onlineconverter.com/mp4-to-gif)

6.  [Site24x7 Link Checker](https://www.site24x7.com/link-checker.html)

7.  [HTML5 Validator](https://validator.w3.org/)

8.  [CSS3 Validator](https://jigsaw.w3.org/css-validator/)

9.  [Axe](https://chrome.google.com/webstore/detail/axe/lhdoppojpmngadmnindnejefpokejbdd?hl=en)

10. [Python 3.6.8](https://www.python.org/)

11. [Node v10.15.1](https://nodejs.org/)

12. [NPM 6.4.1](https://www.npmjs.com/)

13. [Cross Browser Testing](https://crossbrowsertesting.com/)

## Development Environment

[(Back to top)](#table-of-contents)

### windows

    git clone https://github.com/DamianMcNulty/ecommerce.git
    cd ecommerce
    pip install virtualenv
    python -m virtualenv env
    .\env\Scripts\activate
    pip install -r requirements.txt
    python manage.py runserver
    .\env\Scripts\deactivate

### django commands

    django-admin startproject django_auth .
    django-admin startapp accounts
    python3 manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic

## Local Testing

[(Back to top)](#table-of-contents)

    npm i
    npm run cy:open

    python manage.py test

## Cross Browser testing

[(Back to top)](#table-of-contents)

see screenshots in cbt folder

## Deployment

[(Back to top)](#table-of-contents)

    heroku login
    heroku apps
    heroku create damianmcnulty-ecommerce --region eu
    heroku addons:create heroku-postgresql:hobby-dev
    heroku config:set SECRET_KEY="..."
    heroku config:set DATABASE_URL="..."
    heroku config:set DISABLE_COLLECTSTATIC=1
    echo web: gunicorn django_todo.wsgi:application > Procfile
    pip install dj-database-url psycopg2 whitenoise gunicorn Pillow

## Research

[(Back to top)](#table-of-contents)

-   <https://stackoverflow.com/questions/48729966/how-can-i-call-multiple-views-in-one-url-address-in-django>

## Credits

[(Back to top)](#table-of-contents)

## License

See [LICENSE](LICENSE)
