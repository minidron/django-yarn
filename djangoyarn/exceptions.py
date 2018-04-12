from django.core.management.base import CommandError


class YarnNotInstalled(CommandError):
    def __init__(self):
        super().__init__(
            'Yarn not installed, read instruction here - https://yarnpkg.com/',
        )
