from django.conf import settings
from django.core.management.base import BaseCommand

from djangoyarn.exceptions import YarnNotInstalled
from djangoyarn.yarn import yarn_adapter


class BaseYarnCommand(BaseCommand):
    """
    Base management command with yarn support.
    """
    requires_system_checks = False

    def handle(self, *args, **options):
        self._check_yarn_exists()
        yarn_adapter.create_modules_root()

    def _check_yarn_exists(self):
        if not yarn_adapter.is_yarn_exists():
            raise YarnNotInstalled()

    def _install(self, *args):
        yarn_adapter.add(settings.YARN_INSTALLED_APPS, *args)
