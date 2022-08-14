from pathlib import Path
import os
from dotenv import load_dotenv
from vanilladev.settings_debug import *

load_dotenv()

DEBUG = False
ALLOWED_HOSTS = ["vanilla.sh"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DBNAME"),
        'USER': os.getenv("DBUSER"),
        'PASSWORD': os.getenv("DBPASSWD"),
        'HOST': os.getenv("DBHOST"),
    }
}

CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
AWS_S3_ACCESS_KEY_ID = os.getenv("AWSACCESSKEY")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWSSECRET")
AWS_STORAGE_BUCKET_NAME=os.getenv("AWSBUCKET")
AWS_QUERYSTRING_AUTH = False

CSRF_TRUSTED_ORIGINS = ["https://vanilla.sh"]