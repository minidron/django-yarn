import os

from django.conf import settings

__all__ = ['MODULES_ROOT', 'YARN_PATH', 'YARN_FOLDER']


MODULES_ROOT = getattr(settings, 'YARN_MODULES_ROOT',
                       os.path.abspath(os.path.dirname(__name__)))

YARN_PATH = getattr(settings, 'YARN_PATH', 'yarn')

YARN_FOLDER = 'node_modules'
