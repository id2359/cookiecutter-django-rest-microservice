# __author__ = {{cookiecutter.full_name}}
import redis

from .common import Common


class Production(Common):
    env = Common.env

    SECRET_KEY = env('DJANGO_SECRET_KEY')
    DEBUG = False

    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += [
        'gunicorn'
    ]

    ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
    DATABASES = {'default': env.db('DATABASE_URL')}
    DATABASES['default']['ATOMIC_REQUESTS'] = True
    DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)

    ADMIN_URL = env('DJANGO_ADMIN_URL')

    REDIS_POOL = redis.ConnectionPool.from_url(url=f"{env('REDIS_URL')}/1")
    BROKER_URL = f"{env('REDIS_URL')}/0"

    JWT_AUTH = {
        'JWT_SECRET_KEY': env('JWT_SECRET_KEY'),
    }