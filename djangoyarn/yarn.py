import os
import subprocess

from djangoyarn import conf, shortcuts


class YarnAdapter(object):
    """
    Adapter for working with yarn.
    """

    def __init__(self, yarn_path, modules_root):
        self._yarn_path = yarn_path
        self._modules_root = modules_root

    def is_yarn_exists(self):
        """
        Check is yarn installed.
        """
        if (shortcuts.is_executable(self._yarn_path) or
                shortcuts.which(self._yarn_path)):
            return True
        else:
            return False

    def create_modules_root(self):
        """
        Create modules root if need.
        """
        if not os.path.exists(self._modules_root):
            os.makedirs(self._modules_root)

    def call_yarn(self, args):
        """
        Call yarn with a list of args.
        """
        proc = subprocess.Popen([self._yarn_path] + list(args),
                                cwd=self._modules_root)
        proc.wait()

    def add(self, packages, *options):
        """
        Install packages from yarn.
        """
        self.call_yarn(['add'] + list(options) + list(packages))


yarn_adapter = YarnAdapter(conf.YARN_PATH, conf.MODULES_ROOT)
