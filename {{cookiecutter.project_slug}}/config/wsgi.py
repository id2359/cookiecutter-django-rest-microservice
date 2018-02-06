# __author__ = {{cookiecutter.full_name}}

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

from configurations.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
