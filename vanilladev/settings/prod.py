from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRETKEY")
DEBUG = False
ALLOWED_HOSTS = ["194.242.56.216"]

# Application definition
INSTALLED_APPS = [
    'ckeditor',
    'bootstrap5',
    'blog.apps.BlogConfig',
    'home.apps.HomeConfig',
    'media.apps.MediaConfig',
    'login_only_auth.apps.LoginOnlyAuthConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'vanilladev.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"vanilladev","templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'vanilladev.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv("DBNAME"),
        'USER': os.getenv("DBUSER"),
        'PASSWORD': os.getenv("DBPASSWD"),
        'HOST': os.getenv("DBHOST"),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/assets/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "vanilladev", "assets"),
)


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'login_only_auth.User' 
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': '100%'
    }
}

LOGIN_URL = "/user/login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
MEDIA_URL = '/images/'

# TODO: Should be turned on eventually once SSL certificate is installed on server
# CSRF_COOKIE_SECURE=True
# SESSION_COOKIE_SECURE=True