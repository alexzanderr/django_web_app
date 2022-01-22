
import os


from . import BASE_DIR


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