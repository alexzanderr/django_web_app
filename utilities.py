

from random import choice
from string import ascii_letters
from string import digits

def generate_random_token(length=30):
    return "".join([choice(ascii_letters + digits) for _ in range(length)])
