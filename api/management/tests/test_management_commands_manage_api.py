"""
    api/tests/test_management_commands_manage_api.py
"""

from io import StringIO
from django.core.management import call_command
from django.test import TestCase

def print_result(result):
    print("result: '{}'".format(result))

def test_manage_api():
    out = StringIO()
    call_command('manage_api', stdout=out)
    result = out.getvalue().strip()
    assert 'True' == result


def test_manage_api_2():
    out = StringIO()
    call_command('manage_api', stdout=out, third=123)
    result = out.getvalue().strip()

    assert result == "third"
