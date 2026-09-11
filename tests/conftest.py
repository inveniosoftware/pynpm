# SPDX-FileCopyrightText: 2017 CERN.
# SPDX-FileCopyrightText: 2023 Rambaud Pierrick.
# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: BSD-3-Clause

"""Pytest configuration."""

from __future__ import absolute_import, print_function

import json
import shutil
import tempfile
from os.path import dirname, join

import pytest


@pytest.fixture()
def tmpdir():
    """Temporary directory."""
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


@pytest.fixture()
def pkgdir_source():
    """Get source of package directory tests/jspkg/."""
    return join(dirname(__file__), "jspkg")


@pytest.fixture()
def pkg(pkgdir_source, tmpdir):
    """Initialize package directory content."""
    pkgdir = join(tmpdir, "jspkg")
    shutil.copytree(pkgdir_source, pkgdir)
    return join(pkgdir, "package.json")


@pytest.fixture()
def deppkg(tmpdir):
    """Initialize package directory content."""
    src = join(dirname(__file__), "jsdep")
    dst = join(tmpdir, "jsdep")
    shutil.copytree(src, dst)
    return join(dst, "package.json")


@pytest.fixture()
def pkgjson_source(pkgdir_source):
    """Initialize package directory content."""
    with open(join(pkgdir_source, "package.json"), "r") as fp:
        return json.load(fp)
