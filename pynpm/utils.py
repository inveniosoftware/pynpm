# -*- coding: utf-8 -*-
#
# This file is part of PyNPM
# Copyright (C) 2017 CERN.
#
# PyNPM is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Utility function to run NPM."""

from __future__ import absolute_import, print_function

import os
import subprocess
import sys


def run_npm(pkgdir, cmd, args=None, npm_bin='npm', wait=True):
    """Run NPM."""
    command = [npm_bin, cmd] + list(args)
    if wait:
        return subprocess.call(
            command,
            cwd=pkgdir,
        )
    else:
        return subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=pkgdir,
        )
