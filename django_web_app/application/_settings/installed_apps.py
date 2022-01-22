
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
    "postgres_remote",
    "mysql_remote",
    "control_panel",

    # pip install djangorestframework
    "rest_framework",
    "rest_framework.authtoken",
    # pip install django-livereload-server
    "livereload",

    # pip install django-extensions
    # like this './manage.py shell_plus --ptpython'
    "django_extensions",

    # pip install django-debug-toolbar
    "debug_toolbar",
    # pip install django-bower
    "djangobower",
]
