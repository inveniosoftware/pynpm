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

import platform
from os.path import dirname

import pytest

from pynpm import NPMPackage, YarnPackage

# create a global variable to check if we are on windows
# it will pilot the shell option to run the tests
is_windows = platform.system() == "Windows"


def test_version():
    """Test version import."""
    from pynpm import __version__

    assert __version__


def test_package_json(pkg, pkgjson_source):
    """Test package JSON content."""
    npmpkg = NPMPackage(pkg, shell=is_windows)
    assert npmpkg.package_json == pkgjson_source


def test_package_json_path(pkg):
    """Test package JSON content."""
    npmpkg = NPMPackage(pkg, shell=is_windows)
    assert npmpkg.package_json_path == pkg
    npmpkg = NPMPackage(dirname(pkg), shell=is_windows)
    assert npmpkg.package_json_path == pkg


def test_nonexsting_command(pkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg, shell=is_windows)
    pytest.raises(AttributeError, getattr, npmpkg, "cmd_doesnotexists")


def test_disabled_command(pkg):
    """Test command that has been disabled."""
    npmpkg = NPMPackage(pkg, commands=["run-script"], shell=is_windows)
    pytest.raises(AttributeError, getattr, npmpkg, "install")


def test_command(pkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg, shell=is_windows)
    assert npmpkg.run_script("test") == 0


def test_command_nowait(pkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg, shell=is_windows)
    proc = npmpkg.run_script("test", wait=False)
    # Just check output of last line
    for line in proc.stdout:
        pass
    assert line.decode() == "test\n"


def test_command_install(pkg, deppkg):
    """Test non-existing command."""
    npmpkg = NPMPackage(pkg, shell=is_windows)
    assert npmpkg.install() == 0


def test_command_install_yarn(pkg, deppkg):
    """Test yarn install."""
    yarnpkg = YarnPackage(pkg, shell=is_windows)
    assert yarnpkg.install() == 0


@pytest.mark.skipif(not is_windows, reason="Simply check a known Windows bug")
def test_command_windows_fail_without_shell(pkg):
    """Test that command does not work on windows without the shell option."""

    with pytest.raises(FileNotFoundError):
        npmpkg = NPMPackage(pkg)
        assert npmpkg.install() == 0
