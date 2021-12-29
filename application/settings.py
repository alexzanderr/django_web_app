"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

# from credentials import Credentials
from credentials import Configuration# use this for your config
# from example_credentials import Configuration
from pathlib import Path
import json
import os

ProjectStateFile = Path("ProjectState.json")
__state = json.loads(ProjectStateFile.read_text())["state"].split(",")[0].strip().lower()

class Project__:
    def __init__(self, __state: str) -> None:
        if __state == "development":
            self.State = Configuration.Development
        elif __state == "staging":
            self.State = Configuration.Staging
        else:
            self.State = Configuration.Production

Project = Project__(__state)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# ~/Alexzander__/programming/projects/django_web_app/application/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# from ..credentials import Credentials:
SECRET_KEY = Project.State.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = Project.State.DEBUG

ALLOWED_HOSTS = Project.State.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # if this is not here, then you cant access static files
    'django.contrib.staticfiles',

    # apps from this project
    "application",
    "todos",
    "api",  # REST API
    "postgresql_app",
    "telegram",
    "learning.apps.LearningConfig",
    "analytics.apps.AnalyticsConfig",

    # pip install djangorestframework
    "rest_framework",
    "rest_framework.authtoken",
    # pip install django-livereload-server
    "livereload",

    # pip install django-extensions
    # like this './manage.py shell_plus --ptpython'
    "django_extensions",

    # pip install django-debug-toolbar
    "debug_toolbar"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # from django-livereload server
    'livereload.middleware.LiveReloadScript',

    # from django-debug-toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]


SHOW_TOOLBAR_CALLBACK = True

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # the fix was this
            # os.path.join(BASE_DIR, 'todos/templates'),
            # but if the app is installed in INSTALLED_APPS, you dont need this anymore
        ],
        # this means that django will
        # try to search for /templates inside every app that you created with django-admin startapp $appname
        # for this to work you need your $appname in INSTALLED_APPS list
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
    # {
    #     'BACKEND': 'django.template.backends.jinja2.Jinja2',
    #     'DIRS': [
    #         os.path.join(BASE_DIR, 'templates')
    #     ],
    #     "APP_DIRS": True
    # },
]

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {},
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    # django_web_app_postgresql_db
    Project.State.PostgreSQL.DATABASE_AUTH: {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": Project.State.PostgreSQL.DATABASE_AUTH,
        "USER": Project.State.PostgreSQL.USERNAME,
        "PASSWORD": Project.State.PostgreSQL.PASSWORD,
        "HOST": Project.State.PostgreSQL.HOST,
        "PORT": Project.State.PostgreSQL.PORT
    },
    Project.State.PostgreSQL.DATABASE_DJANGO: {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": Project.State.PostgreSQL.DATABASE_DJANGO,
        "USER": Project.State.PostgreSQL.USERNAME,
        "PASSWORD": Project.State.PostgreSQL.PASSWORD,
        "HOST": Project.State.PostgreSQL.HOST,
        "PORT": Project.State.PostgreSQL.PORT
    },
    # django_web_app_mongo_db
    Project.State.MongoDB.DATABASE_DJANGO: {
        "ENGINE": "djongo",
        "NAME": Project.State.MongoDB.DATABASE_DJANGO,
        "CLIENT": {
            "host": Project.State.MongoDB.HOST,
            "port": Project.State.MongoDB.PORT,
            "username": Project.State.MongoDB.USERNAME,
            "password": Project.State.MongoDB.PASSWORD,
            "authSource": Project.State.MongoDB.AUTHSOURCE
        }
    },
    Project.State.MySQL.DATABASE_DJANGO: {
        "ENGINE": "django.db.backends.mysql",
        "NAME": Project.State.MySQL.DATABASE_DJANGO,
        "USER": Project.State.MySQL.USERNAME,
        "PASSWORD": Project.State.MySQL.PASSWORD,
        "HOST": Project.State.MySQL.HOST,
        "PORT": Project.State.MySQL.PORT
    }
}


DATABASE_ROUTERS = [
    "routers.database_routers.AuthRouter",
    "routers.database_routers.PostgresqlRouter",
    "routers.database_routers.MongodbRouter",
    "routers.database_routers.MySQLRouter",
]


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# static root is for
# python manage.py collectstatic
# these files need to be server to nginx
# gunicorn doesnt server static files
# neither django, just the runserver
STATIC_ROOT = os.path.join(BASE_DIR, "nginx/static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # without this it doesnt work
    os.path.join(BASE_DIR, "static/logo"),
]

mini_apps = [
    "todos",
    "api"
]
STATICFILES_DIRS.extend([
    # maybe ? it works
    os.path.join(BASE_DIR, f"{app}/static") for app in mini_apps
])

# asta era problema pentru static
# STATICFILES_FINDERS = [
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder'
# ]

# these dont work
# this should handle extra slash at the end of url
# APPEND_SLASH = True
# PREPEND_WWW = False

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        "rest_framework.permissions.DjangoModelPermissions",
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.permissions.IsAdminUser'
    ],
}

# for django-redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        # 1 is database number
        # redis has from 0 to 15 (16 total)
        # "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


LIVERELOAD_HOST="localhost"
LIVERELOAD_PORT="5554"

# Always use ptpython for shell_plus
SHELL_PLUS = "ptpython"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"rich": {"datefmt": "[%X]"}},
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "formatter": "rich",
            "level": "DEBUG",

            # not working
            # "rich_traceback": True,
        },
        # not working
        # "file": {
        #     "class": "rich.logging.RichHandler",
        #     "filename": "logs/dev_server/logs.log",
        #     "level": "DEBUG",
        # }
    },
    "loggers": {"django": {"handlers": ["console"]}},
}

# for debug-toolbar
INTERNAL_IPS = [
    "*",
    # "127.0.0.1",
    # ...
]