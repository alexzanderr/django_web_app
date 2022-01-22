

from . import PROJECT_ROOT


BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
)
# https://pypi.org/project/django-bower/
BOWER_COMPONENTS_ROOT = (PROJECT_ROOT / 'components').absolute().as_posix()
BOWER_PATH = (PROJECT_ROOT / 'node_modules/.bin/bower').absolute().as_posix()