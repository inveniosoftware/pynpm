# -*- coding: utf-8 -*-
#
# This file is part of PyNPM
# Copyright (C) 2017 CERN.
#
# PyNPM is free software; you can redistribute it and/or modify
# it under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from os.path import dirname

import pytest

from pynpm import NPMPackage, YarnPackage


def test_version():
    """Test version import."""
    from pynpm import __version__
    assert __version__


def test_package_json(pkg, pkgjson_source):
    """Test package JSON content."""
    npmpkg = NPMPackage(pkg)
    assert npmpkg.package_json == pkgjson_source


def test_package_json_path(pkg):
    """Test package JSON content."""
    npmpkg = NPMPackage(pkg)
    assert npmpkg.package_json_path == pkg
    npmpkg = NPMPackage(dirname(pkg))
    assert npmpkg.package_json_path == pkg


def test_nonexsting_command(pkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg)
    pytest.raises(AttributeError, getattr, npmpkg, 'cmd_doesnotexists')


def test_disabled_command(pkg):
    """Test command that has been disabled."""
    npmpkg = NPMPackage(pkg, commands=['run-script'])
    pytest.raises(AttributeError, getattr, npmpkg, 'install')


def test_command(pkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg)
    assert npmpkg.run_script('test') == 0


def test_command_nowait(pkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg)
    proc = npmpkg.run_script('test', wait=False)
    # Just check output of last line
    for l in proc.stdout:
        pass
    assert l.decode() == u'test\n'


def test_command_install(pkg, deppkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg)
    assert npmpkg.install() == 0


def test_command_install_yarn(pkg, deppkg):
    """Test yarn install."""
    yarnpkg = YarnPackage(pkg)
    assert yarnpkg.install() == 0
