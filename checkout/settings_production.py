import os

from .settings import *

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

STATIC_URL = '/site_media/static/'

CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
