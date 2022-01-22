
import sys
import os
from pathlib import Path

# ~/Alexzander__/programming/projects/django_web_app/django_web_app/application/_settings/templates.py
BASE_DIR = os.path.abspath(__file__)
for _ in range(3):
    BASE_DIR = os.path.dirname(BASE_DIR)

print(BASE_DIR)
PROJECT_ROOT = Path(BASE_DIR)


from .templates import TEMPLATES
from .installed_apps import INSTALLED_APPS
from .middleware import MIDDLEWARE
from .logging_ import LOGGING
from .caches import CACHES
from .bower import BOWER_COMPONENTS_ROOT
from .bower import BOWER_PATH
from .bower import BOWER_INSTALLED_APPS

def export(fn):
    mod = sys.modules[fn.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
    return fn


_locals = locals().copy()
# for loco in _locals:
#     if loco.isupper():
#         print(loco)


# exporting only uppercase variables
# because we need only them
__all__ = [loco for loco in _locals if loco.isupper()]
