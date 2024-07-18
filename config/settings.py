import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

PATH_DB = BASE_DIR / '.env'
load_dotenv(PATH_DB)
PASSWORD_DB = os.getenv('PASSWORD_DB')
USER_DB = os.getenv('USER_DB')
NAME_DB = os.getenv('NAME_DB')

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv("DEBUG", False) == "True"

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'django_celery_beat',
    'corsheaders',

    'users',
    'habits',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": NAME_DB,  # Название БД
        "USER": USER_DB,  # Пользователь для подключения
        "PASSWORD": PASSWORD_DB,  # Пароль для этого пользователя
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
    }
}

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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_TRACK_STARTED = os.getenv(
    "CELERY_TASK_TRACK_STARTED", False) == 'True'
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BEAT_SCHEDULE = {
    "send_remainder": {
        "task": "habits.tasks.send_remainder",
        "schedule": timedelta(minutes=1),
    },
}
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.telegram.org/bot'

CORS_ALLOWED_ORIGINS = ['http://localhost:8000',]
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000',]
CORS_ALLOW_ALL_ORIGINS = False
