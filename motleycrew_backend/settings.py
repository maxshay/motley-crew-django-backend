"""
Django settings for motleycrew_backend project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
import datetime
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# env vars
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_key = os.getenv('SECRET_KEY')
if secret_key is None:
  raise KeyError(f'SECRET_KEY env var does not exist')
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
dev_env = os.getenv('DEV_ENV')
if dev_env is None:
  raise KeyError(f'DEV_ENV env var does not exist')

DEBUG = dev_env == 'dev'

if DEBUG:
  ALLOWED_HOSTS = ['*']
else:

  ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'mcbackenddev.herokuapp.com']

# Application definition
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'corsheaders',
  'rest_framework',
  'users',
  'folders',
  'files',
  'route_slips',
  'route_items',
  'form_fields',
  'messages.apps.MessagesConfig'
]

MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
]


CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://127.0.0.1:3000', 'https://motleycrewdev.com']
# CORS_ORIGIN_WHITELIST = ['http://localhost:3000', 'http://127.0.0.1:3000', 'https://motleycrewdev.com']

ROOT_URLCONF = 'motleycrew_backend.urls'

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

WSGI_APPLICATION = 'motleycrew_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

postgresdb_name = os.getenv('POSTGRES_NAME')
postgresdb_host = os.getenv('POSTGRES_HOST')
postgresdb_user = os.getenv('POSTGRES_USER')
postgresdb_pass = os.getenv('POSTGRES_PASSWORD')
postgresdb_port = os.getenv('POSTGRES_PORT')

if postgresdb_name is None:
  raise KeyError(f'POSTGRES_NAME env var does not exist')
if postgresdb_host is None:
  raise KeyError(f'POSTGRES_HOST env var does not exist')
if postgresdb_user is None:
  raise KeyError(f'POSTGRES_USER env var does not exist')
if postgresdb_pass is None:
  raise KeyError(f'POSTGRES_PASSWORD env var does not exist')
if postgresdb_port is None:
  raise KeyError(f'POSTGRES_PORT env var does not exist')


AVAILABLE_DATABAES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': postgresdb_name,
    'HOST': postgresdb_host,
    'USER': postgresdb_user,
    'PASSWORD': postgresdb_pass,
    'PORT': postgresdb_port,
  },
  'testing': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'test',
    'HOST': 'localhost',
    'USER': 'test',
    'PASSWORD': 'test',
    'PORT': '5432',
  },
}

if 'test' in sys.argv:
  DATABASES = {'default': AVAILABLE_DATABAES['testing']}
else:
  DATABASES = {'default': AVAILABLE_DATABAES['default']}


redis_url = os.getenv('REDIS_TLS_URL')
if redis_url is None:
  raise KeyError(f'REDIS_TLS_URL env var does not exist')

CACHES = {
  'default': {
    'BACKEND': 'django_redis.cache.RedisCache',
    'LOCATION': redis_url,
    'OPTIONS': {
      'CLIENT_CLASS': 'django_redis.client.DefaultClient',
      'CONNECTION_POOL_KWARGS': {'ssl_cert_reqs': None}
    },
    'KEY_PREFIX': 'mc'
  }
}


REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'rest_framework.authentication.SessionAuthentication',
  ],
  'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated'
  ]
}

SIMPLE_JWT = {
  'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=365),
  'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=365),
  'USER_ID_CLAIM': 'id',
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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

AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_ACCESS_KEY_ID=os.getenv('AWS_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY=os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE=False