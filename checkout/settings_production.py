import os

from .settings import *

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

STATIC_URL = '/site_media/static/'

CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = int(os.environ['EMAIL_PORT'])
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
