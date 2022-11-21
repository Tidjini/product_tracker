"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

import asyncio

# import threading

from django.core.wsgi import get_wsgi_application

from apps.core import client

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()


# some = threading.Event()


# def run_socket():
#     some.set()
asyncio.run(client.main())


# run_socket()
# # t = Thread(target=run_socket)
# # t.run()
