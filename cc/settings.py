"""
Django settings for cc project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import json
import socket
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '-(aj!gv6h(x*d27$(ss&5v8&i&^6ze0m*ozllibrpiplo98)ee'
SECRET_KEY=os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['passedonwisdom.herokuapp.com','127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'ccapp.apps.CcappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages'
]

print(socket.gethostname())
if (socket.gethostname()!='LAPTOP-JP8NL3R2'):
    SECURE_SSL_REDIRECT = True # [1]
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'cc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'cc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WHITENOISE_USE_FINDERS=True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'passedonwisdom@gmail.com' 
EMAIL_HOST_PASSWORD = 'campusCompany@321'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#media stuff
# MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

# temp google cloud 

# DEFAULT_FILE_STORAGE='ccapp.gCloud.GoogleCloudMediaFileStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_PROJECT_ID = 'passedon'
GS_BUCKET_NAME = 'passedon3'
MEDIA_ROOT = "media/"
# MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)


from google.oauth2 import service_account
credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
if credentials_raw:
    service_account_info = json.loads(credentials_raw)
    GS_CREDENTIALS=service_account.Credentials.from_service_account_info(
        service_account_info)
else:
    GS_CREDENTIALS=service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR,'key/passedon-09fd83b98745.json'))


# from django.conf import settings
# from storages.backends.gcloud import GoogleCloudStorage
# from storages.utils import setting
# from urllib.parse import urljoin


# class GoogleCloudMediaFileStorage(GoogleCloudStorage):
#        """
#          Google file storage class which gives a media file path from       MEDIA_URL not google generated one.
#        """
#         bucket_name = setting('GS_BUCKET_NAME')
#         def url(self, name):
#             """
#             Gives correct MEDIA_URL and not google generated url.
#             """
#             return urljoin(settings.MEDIA_URL, name) a
