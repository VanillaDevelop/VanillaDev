from pathlib import Path
import os
from dotenv import load_dotenv
from settings.debug import *

load_dotenv()

DEBUG = False
ALLOWED_HOSTS = [".vanilla-dev.online"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DBNAME"),
        'USER': os.getenv("DBUSER"),
        'PASSWORD': os.getenv("DBPASSWD"),
        'HOST': os.getenv("DBHOST"),
    }
}

CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True