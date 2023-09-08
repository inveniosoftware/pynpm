=======
 PyNPM
=======

.. image:: https://github.com/inveniosoftware/pynpm/workflows/CI/badge.svg
        :target: https://github.com/inveniosoftware/pynpm/actions?query=workflow%3ACI

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

Trouble shooting
================

Windows user may face the following error when running the ``NPM`` command:

.. code-block:: console

    [WinError 2] The system cannot find the file specified

It means supbrossess is unable to run the specific command. To fix this issue, 
use the ``shell=True`` option uppon class initialization:

.. code-block:: python

    pkg = NPMPackage('path/to/package.json', shell=True)

.. danger:: 

    This option is not recommended for security reasons. It should only be used
    on trusted inputs.
