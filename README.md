## About This Project
This project is a django-based, CMS-style web presence I am using for my personal website, [Vanilla Develop](https://vanilla.sh). It is not intended to be an end-user friendly CMS which allows for the creation of different types of layouts and website styles, but rather mirrors my personal taste for what I want my portfolio website to look like. As such, you are free to customize it to your liking and use it as a framework for your personal projects. However, **do not reupload this project without making significant changes to it, and remove any relation to my name from the project before hosting this website for your personal use case.**

This repository features a django project (in the directory `vanilladev/`), as well as a Bootstrap Studio file (`vanilladev.bsdesign`) and its corresponding output (`bsdesign-output/`). The bootstrap studio file contains rough templates/mockups of most of the pages, and is where I extract the `styles.css` file from, which contains all custom css styles that are not provided by Bootstrap. The `requirements.txt` file contains all python packages required to host the project. The project is hosted using Python 3.9.

Not included in the GitHub repository is a `.env` file in the main directory. This includes the following keys:
```
DBHOST="{{Postgres Database Host}}
DBUSER="{{Postgres Database User}}"
DBNAME="{{Postgres Database Name}}"
DBPASSWD="{{Postgres Database Password}}"
SECRETKEY="{{Django Secret Key}}"
AWSACCESSKEY="{{AWS Access Key for S3 Management User}}"
AWSSECRET="{{AWS Secret for S3 Management User}}"
AWSBUCKET="{{AWS S3 Bucket Name}}"
```
Please note that these environment variables need to be provided in some form for the program to establish a database connection and function properly. The Postgres database can be set up in the usual Django way when the environment variables are properly provided (`python manage.py makemigrations` followed by `python manage.py migrate`).

Two setting files are provided, `vanilladev.settings` and `vanilladev.settings_debug`, respectively for a production and debugging environment. The most notable differences between the two being whether or not the django debug environment is activated, and the allowed hosts (the debug setting allows all hosts, the production setting only allows my webserver to host the page). Additionally, Some further changes exist in the production version, such as the CSRF policy and HTTPS redirects. The production version connects to the Postgres database and S3 bucket configured in the environment variables, while the debug version uses a local sqlite database and local file storage.

In general, the settings (prod) file inherits values from the settings_debug file, unless they are overwritten. If you want a setting to be available in both debugging and production, add it to the `vanilladev.settings_debug` file. The production environment is the default environment when starting the application. To start with debug settings, run `python manage.py runserver --settings=vanilladev.settings_debug`.

### Main Project (vanilladev)
The main project is in the `vanilladev/vanilladev` directory. This is where the other apps are hooked into, including URL mappings. It also includes a static files directory `vanilladev/vanilladev/assets`, as well as a templates directory `vanilladev/vanilladev/templates` which contains the template `base.html`. This is the main html template that is used by most pages, containing styling and js includes, header, footer, and the common navbar.

### Authentication and Authorization (login_only_auth module)
As I've written this website for my personal needs, no separate levels of authorization exist. All users are authorized to change all articles, blog posts and projects on the website. Further, there is no registration system, as users should not change over the lifecycle of the system, and if they do, can simply be created programmatically. To create a user, you may do so programmatically by importing `User` from `login_only_auth.models` and calling the [create_user helper function](https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user). Existing users can then log in via the path `/user/login`. Any logged in user can see draft projects, articles and blog posts, edit and delete existing ones, and create new ones. A user can logout using `/user/logout`. 

When logged in, the main navbar also changes to reflect the additional URL paths that logged in users have access to.

In terms of password security, the default [Django encryption](https://en.wikipedia.org/wiki/PBKDF2) is used, which consists of iterative SHA256-based salted password hashing. This should be considered very secure for most end-user cases. 

### Home Page (home module)
This is the simplest app module which serves the main URL path `/` (i.e., the home page). Logged in users may update the four most recent project excerpts which are shown on the home page.

### Blog (blog module)
This module serves pages via the path `/blog/`. It contains a paginated blog overview (`/blog/overview`), add, edit and deletion paths for logged in users, and the ability to display blog posts. When adding or editing a blog post, the content field is presented via a [ckeditor](https://ckeditor.com/) field, and the raw HTML is displayed within the template when viewing the finished post. **The content of a blogpost is considered safe in this application without further security checks, as no unauthorized person should be able to create new posts or edit existing ones. Please consider this before making this model available to a more widespread audience.** Further, categories for blogposts can be added or removed using the `/blog/categories`.

### Projects (projects module)
This module serves pages via the path `/projects/`. It contains an overview of projects and the ability to add, edit and delete projects for logged in users. The overview can be found via the navbar when logged in, and all projects that are not drafts will also be automatically added to the navbar for all users. Unlike blog posts, projects follow a more rigid structure, and have several ckeditor fields that must be filled before creating a new project. 

### Articles (articles module)
The articles module serves pages via the path `/articles/`, and functions much like the projects module. Articles are essentially projects with a different structure. They offer the same options for logged in users when it comes to adding, editing, and deleting them.

### Media Upload (media module)
This module features image upload for logged in users to the S3 bucket configured in the environment variables. Again, users can add, edit, and delete images from the server. 

### "Other Work" (sideprojects module)
The sideprojects module maps to the `/side` path. It is most comparable to the home page. The main page itself is static, but features dynamic integration of cards for three different types of projects (professional work, side projects, and treasure trove). Logged in users can add, edit and delete the corresponding cards.