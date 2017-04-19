# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

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
