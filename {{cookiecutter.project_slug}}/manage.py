#!/usr/bin/env python
# __author__ = {{cookiecutter.full_name}}

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
