import os
import sys


def main() -> None:
    """
    Run administrative tasks for the Django project.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
