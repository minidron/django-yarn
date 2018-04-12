from djangoyarn.management.base import BaseYarnCommand

from djangoyarn.yarn import yarn_adapter


class Command(BaseYarnCommand):
    help = 'Call yarn in modules root ({}).'.format(yarn_adapter._modules_root)

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='+', type=str)

    def handle(self, *args, **options):
        super().handle(*args, **options)
        args = args or tuple(options.pop('command'))
        if self._is_single_command('install', args):
            self._install()
        else:
            yarn_adapter.call_yarn(args)

    def _is_single_command(self, name, args):
        return len(args) == 1 and args[0] == name
