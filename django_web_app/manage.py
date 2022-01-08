#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from rich.traceback import install
install(show_locals=False)


def main():
    # print(sys.path)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


    from rich.console import Console
    _console = Console()
    try:
        execute_from_command_line(sys.argv)
    except Exception:
        _console.print_exception(
        show_locals=True,
        word_wrap=True)


if __name__ == '__main__':
    main()
