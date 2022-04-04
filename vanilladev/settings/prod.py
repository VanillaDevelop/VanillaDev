from pathlib import Path
import os
from dotenv import load_dotenv
from settings.debug import *

load_dotenv()

DEBUG = False
ALLOWED_HOSTS = ["194.242.56.216"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DBNAME"),
        'USER': os.getenv("DBUSER"),
        'PASSWORD': os.getenv("DBPASSWD"),
        'HOST': os.getenv("DBHOST"),
    }
}

# TODO: Should be turned on eventually once SSL certificate is installed on server
# CSRF_COOKIE_SECURE=True
# SESSION_COOKIE_SECURE=True