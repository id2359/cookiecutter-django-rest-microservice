# __author__ = {{cookiecutter.full_name}}
import djcelery
import environ
from configurations import Configuration


class Common(Configuration):
    ROOT_DIR = environ.Path(__file__) - 3
    # Load operating system environment variables and then prepare to use them
    env = environ.Env()

    MANAGERS = ADMINS = [("{{cookiecutter.github_username}}", "{{cookiecutter.email}}"), ]

    INSTALLED_APPS = [
        # Default Django apps:
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Third-part
        'rest_framework',
        'djcelery',
        'rest_framework_filters',
        # local apps
        'api'
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = str(ROOT_DIR.path('staticfiles'))
    STATICFILES_DIRS = []
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    JET_SIDE_MENU_COMPACT = True

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': STATICFILES_DIRS,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    ROOT_URLCONF = 'config.urls'

    WSGI_APPLICATION = 'config.wsgi.application'

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    LANGUAGE_CODE = 'zh-hans'

    TIME_ZONE = 'Asia/Shanghai'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS':
            'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE':
            10,
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
        'DEFAULT_FILTER_BACKENDS': ('rest_framework_filters.backends.DjangoFilterBackend',),
    }

    LOG_DIR = ROOT_DIR.path('logs')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard_bak': {
                'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
            },
            'standard': {
                'format': '[%(asctime)s] [%(threadName)s:%(thread)d:%(name)s] '
                          '[%(levelname)s] [%(module)s.%(funcName)s Line:%(lineno)d]- %(message)s'
            },
        },
        'filters': {
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': str(LOG_DIR.path('default.log')),
                'backupCount': 5,
                'formatter': 'standard',
                'interval': 1,
                'when': 'D',
                'delay': True
            },
            'worker': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': str(LOG_DIR.path('work.log')),
                'backupCount': 5,
                'formatter': 'standard',
                'interval': 1,
                'when': 'D',
                'delay': True
            },
            'error': {
                'level': 'ERROR',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': str(LOG_DIR.path('error.log')),
                'backupCount': 5,
                'formatter': 'standard',
                'interval': 1,
                'when': 'D',
                'delay': True
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['default', 'console', 'error'],
                'level': 'DEBUG',
                'propagate': False
            },
            'worker': {
                'handlers': ['worker', 'console', 'error'],
                'level': 'INFO',
                'propagate': False
            },
        }
    }
    djcelery.setup_loader()
    CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_TASK_IGNORE_RESULT = True
