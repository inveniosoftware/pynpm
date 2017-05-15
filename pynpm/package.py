# -*- coding: utf-8 -*-
#
# This file is part of PyNPM
# Copyright (C) 2017 CERN.
#
# PyNPM is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Python interface to your NPM and package.json."""

from __future__ import absolute_import, print_function

import json
from functools import partial
from os.path import basename, dirname, join

from .utils import run_npm


class NPMPackage(object):
    """API to an NPM ``package.json``.

    :param filepath: Path to ``package.json`` or directory containing the file.
    :param npm_bin: Path to NPM binary. Defaults to ``npm``.
    :param commands: List of allowed NPM commands to invoke.
    """

    def __init__(self, filepath, npm_bin='npm', commands=None):
        """Initialize package."""
        self._commands = commands or [
            'build',
            'init',
            'install',
            'link',
            'run-script',
            'start',
            'stop',
            'test',
        ]
        self._package_json_path = filepath
        self._package_json_contents = None
        self._npm_bin = npm_bin

    @property
    def package_json_path(self):
        """Get ``package.json`` file path."""
        if basename(self._package_json_path) != 'package.json':
            return join(self._package_json_path, 'package.json')
        return self._package_json_path

    @property
    def package_json(self):
        """Read ``package.json`` contents."""
        if self._package_json_contents is None:
            with open(self.package_json_path, 'r') as fp:
                self._package_json_contents = json.load(fp)
        return self._package_json_contents

    def _run_npm(self, command, *args, **kwargs):
        """Run an NPM command.

        By default the call is blocking until NPM is finished and output
        is directed to stdout. If ``wait=False`` is passed to the method,
        you get a handle to the process (return value of ``subprocess.Popen``).

        :param command: NPM command to run.
        :param args: List of arguments.
        :param wait: Wait for NPM command to finish. By defaul
        """
        return run_npm(
            dirname(self.package_json_path),
            command,
            npm_bin=self._npm_bin,
            args=args,
            **kwargs
        )

    def __getattr__(self, name):
        """Run partial function for an NPM command."""
        name = name.replace('_', '-')
        if name in self._commands:
            return partial(self._run_npm, name)
        raise AttributeError('Invalid NPM command.')


class YarnPackage(NPMPackage):
    """Yarn package."""

    def __init__(self, filepath, yarn_bin='yarn', commands=None):
        """Initialize package."""
        super(YarnPackage, self).__init__(
            filepath,
            npm_bin=yarn_bin,
            commands=commands or ['install']
        )
