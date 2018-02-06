# __author__ = {{cookiecutter.full_name}}

import environ
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

env = environ.Env()

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = env('SU_USERNAME', default='{{cookiecutter.github_username}}')
        if User.objects.filter(username=username).exists():
            return

        password = env('SU_PASSWORD', default='{{cookiecutter.github_username}}')
        email = env('SU_EMAIL', default='{{cookiecutter.email}}')

        User.objects.create_superuser(username=username, password=password, email=email)
        self.stdout.write(f"superuser {username} created")
