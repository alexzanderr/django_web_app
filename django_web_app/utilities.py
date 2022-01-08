

from random import choice
from string import ascii_letters
from string import digits

def generate_random_token(length=30):
    return "".join([choice(ascii_letters + digits) for _ in range(length)])


def _get_conf():
    try:
        from credentials import Configuration as _conf
    except (ModuleNotFoundError, ImportError):
        from remote_credentials import Configuration as _conf

    return _conf
