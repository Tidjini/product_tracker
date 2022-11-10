from .base import *

# SECRET_KEY = "1%5m=_#%m$tu-s*5=gxpwrpu7u$5l1b*r$k#$xeh-i=%&x2z+3"

DEBUG = True
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.local.sqlite3",
    }
}
