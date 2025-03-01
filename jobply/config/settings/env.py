import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--h3q_f+4v+o(o7dkvoe&xa#4obm8tt$nzttpzfe4z@+c%8q^ui'

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Test email credential mailtrap
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '4ce08afa4b9133'
EMAIL_HOST_PASSWORD = 'f272f01a369232'
EMAIL_PORT = '2525'

FROM_EMAIL = "jobply<noreply@jobply.com>"
