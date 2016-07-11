"""
WSGI config for test1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/admin/test1/test1')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")

application = get_wsgi_application()
