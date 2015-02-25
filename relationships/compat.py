import django


# Django 1.5 add support for custom auth user model
from django.conf import settings

if django.VERSION >= (1, 5):
    AUTH_USER_MODEL = settings.AUTH_USER_MODEL
else:
    try:
        from django.contrib.auth.models import User
        AUTH_USER_MODEL = 'auth.User'
    except ImportError:
        raise ImportError(u"User model is not to be found.")

# location of patterns, url, include changes in 1.4 onwards
try:
    from django.conf.urls import patterns, url, include
except:
    from django.conf.urls.defaults import patterns, url, include
