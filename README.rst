..
    This file is part of Invenio.
    Copyright (C) 2017 CERN.

    Invenio is free software; you can redistribute it
    and/or modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation; either version 2 of the
    License, or (at your option) any later version.

    Invenio is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Invenio; if not, write to the
    Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
    MA 02111-1307, USA.

    In applying this license, CERN does not
    waive the privileges and immunities granted to it by virtue of its status
    as an Intergovernmental Organization or submit itself to any jurisdiction.

=======
 PyNPM
=======

.. image:: https://img.shields.io/travis/inveniosoftware/pynpm.svg
        :target: https://travis-ci.org/inveniosoftware/pynpm

.. image:: https://img.shields.io/coveralls/inveniosoftware/pynpm.svg
        :target: https://coveralls.io/r/inveniosoftware/pynpm

.. image:: https://img.shields.io/github/tag/inveniosoftware/pynpm.svg
        :target: https://github.com/inveniosoftware/pynpm/releases

.. image:: https://img.shields.io/pypi/dm/pynpm.svg
        :target: https://pypi.python.org/pypi/pynpm

.. image:: https://img.shields.io/github/license/inveniosoftware/pynpm.svg
        :target: https://github.com/inveniosoftware/pynpm/blob/master/LICENSE

Python interface to your NPM and package.json.

Further documentation is available on https://pynpm.readthedocs.io/.

Installation
============

PyNPM is on PyPI so all you need is:

.. code-block:: console

   $ pip install pynpm

Usage
=====

First point PyNPM to your ``package.json``:

.. code-block:: python

    from pynpm import NPMPackage
    pkg = NPMPackage('path/to/package.json')

Now you can run e.g. ``npm install`` from within Python:

.. code-block:: python

    pkg.install()

Arguments are also support so you can run e.g. ``npm run build --report``:

.. code-block:: python

    pkg.run_script('build', '--report')

Want to use ``yarn`` instead?

.. code-block:: python

    from pynpm import YarnPackage
    pkg = YarnPackage('path/to/package.json')
    pkg.install()

By default NPM output is piped through and the function call will wait for NPM
to finish. If you want to silence the output or interact with process pass
``wait=False`` and you will get a subprocess.POpen object back:

.. code-block:: python

    p = pkg.install(wait=False)
    p.wait()

By default you can run the following NPM commands:

* ``build``
* ``init``
* ``install``
* ``link``
* ``run-script``
* ``start``
* ``stop``
* ``test``

You can also run other NPM commands or restrict which commands you can run:

.. code-block:: python

    pkg = NPMPackage('path/to/package.json', commands=['install'])
