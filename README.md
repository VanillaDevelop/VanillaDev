## About This Project
This project is a django-based, CMS-style web presence I will be using for my personal website, [Vanilla Develop](https://vanilla-dev.online). It is not intended to be an end-user friendly CMS which allows for the creation of different types of layouts and website styles, but rather mirrors my personal taste for what I want my portfolio website to look like. As such, you are free to customize it to your liking and use it as a framework for your personal projects. However, **do not reupload this project without making significant changes to it, and remove any relation to my name from the project before hosting this project for your personal circumstances.**

This repository features a django project (in the directory `vanilladev/`), as well as a Bootstrap Studio file (`vanilladev.bsdesign`) and its corresponding output (`bsdesign-output/`). The bootstrap studio file contains rough templates/mockups of most of the pages, and is where I extract the `styles.css` file from, which hosts all custom css styles that are not provided by Bootstrap. The `requirements.txt` file contains all python packages required to host the project. The project is hosted using Python 3.7.

Not included in the GitHub repository is a `.env` file in the main directory. This includes the following keys:
```
DBHOST = "{{Database Host IP}}"
DBUSER = "{{Database User Name}}"
DBNAME = "{{Database Name}}"
DBPASSWD = "{{Database User Password}}"
SECRETKEY = "{{Django Secret Key}}"
```
Please note that these environment variables need to be provided in some form for the program to establish a database connection and function properly. The MySQL database can be configured in the usual Django way when the environment variables are properly provided (`python manage.py makemigrations` followed by `python manage.py migrate`).

Two setting files are provided, `settings.debug` and `settings.prod`, respectively for a debugging and production environment. The most notable differences between the two being whether or not the django debug environment is activated, and the allowed hosts (the debug setting allows all hosts, the production setting only allows my webserver to host the page. You may need to adapt this setting if you choose to reuse this settings file for your own purposes).

The django project consists of multiple apps, each responsible for certain functionality, which are listed below.

### Main Project (vanilladev)
The main project is in the `vanilladev/vanilladev` directory. This is where the other apps are hooked into, including URL mappings. It also includes a static files directory `vanilladev/vanilladev/assets`, as well as a templates directory `vanilladev/vanilladev/templates` which contains the template `base.html`. This is the main html template that is used by most pages, containing styling and js includes, header, footer, and the common navbar.

### Authentication and Authorization (login_only_auth module)
As I've written this website for my personal needs, no separate levels of authorization exist. All users are authorized to change all articles, blog posts and projects on the website. Further, there is no registration system, as users should not change over the lifecycle of the system, and if they do, can simply be created programmatically. To create a user, you may do so programmatically by importing `User` from `login_only_auth.models` and calling the [create_user helper function](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user). Existing users can then log in via the path `/user/login`. Any logged in user can see draft projects, articles and blog posts, edit and delete existing ones, and create new ones. A user can logout using `/user/logout`. These paths cannot be reached via the navbar, as it is unnecessary to expose the CMS style design of the page for my use case.

In terms of password security, the default [Django encryption](https://en.wikipedia.org/wiki/PBKDF2) is used, which consists of iterative SHA256-based salted password hashing. This should be considered secure for most end-user cases. 

### Home Page (home module)
This is the simplest app module which only serves static pages via the path `/` (i.e., the home page). This page currently allows for no customization outside of changing the source code.

### Blog (blog module)
This module serves pages via the path `/blog/`. It contains a paginated blog overview (`/blog/overview`), add, edit and deletion paths for logged in users, and the ability to display blog posts. When adding or editing a blog post, the content field is presented via a [ckeditor](https://ckeditor.com/) field, and the raw HTML is displayed within the template when viewing it. **The content of a blogpost is considered safe in this application without checking, as no unauthorized person should be able to create new posts or edit existing ones. Please consider this when making this model available to a more widespread audience.** Further, categories for blogposts can be added or removed using the `/blog/categories`.

### Projects (projects module)
This module serves pages via the path `/projects/`. It contains an overview of projects and the ability to add, edit and delete projects for logged in users. The overview can be found via the navbar when logged in, and all projects that are not drafts will also be automatically added to the navbar for all users. Unlike blog posts, projects follow a more rigid structure, and have several ckeditor fields that must be filled before creating a new project. 