"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from . import Credentials
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# ~/Alexzander__/programming/projects/django_web_app/application/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# from ..credentials import Credentials
SECRET_KEY = Credentials.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = Credentials.DEBUG

ALLOWED_HOSTS = []


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
    "todos",
    "api",  # REST API

    # pip install djangorestframework
    "rest_framework"
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

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # the fix was this
            # os.path.join(BASE_DIR, 'todos/templates'),
            # but if the app is installed, you dont need this anymore
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
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

# STATIC_ROOT = os.path.join(BASE_DIR, "static/")


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
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly' not working
        "rest_framework.permissions.DjangoModelPermissions"
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser'
    ]
}
