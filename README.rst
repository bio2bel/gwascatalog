Bio2BEL GWAS Catalog |build|
==================================================
The NHGRI-EBI Catalog of published genome-wide association studies.

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_gwascatalog`` can be installed easily from
`PyPI <https://pypi.python.org/pypi/bio2bel_gwascatalog>`_
with the following code in your favorite terminal:

from the latest code on `GitHub <https://github.com/bio2bel/gwascatalog>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/gwascatalog.git

Setup
-----
GWAS Catalog can be downloaded and populated from either the
Python REPL or the automatically installed command line utility.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_gwascatalog
    >>> gwascatalog_manager = bio2bel_gwascatalog.Manager()
    >>> gwascatalog_manager.populate()

Command Line Utility
~~~~~~~~~~~~~~~~~~~~
.. code-block:: sh

    bio2bel_gwascatalog populate


.. |build| image:: https://travis-ci.com/bio2bel/gwascatalog.svg?branch=master
    :target: https://travis-ci.com/bio2bel/gwascatalog
    :alt: Build Status

.. |documentation| image:: http://readthedocs.org/projects/bio2bel-gwascatalog/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/gwascatalog/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_gwascatalog.svg
    :alt: Current version on PyPI

.. |coverage| image:: https://codecov.io/gh/bio2bel/gwascatalog/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/gwascatalog?branch=master
    :alt: Coverage Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_gwascatalog.svg
    :alt: Stable Supported Python Versions

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_gwascatalog.svg
    :alt: MIT License
