
ecashaddress
============

``ecashaddress`` is python library which is able to convert legacy
bitcoin addresses to the cashaddress format, and convert between various
cashaddr prefixes.

It also provides a command line tool for converting address formats:
``ecashconvert``

Installation
============

To install this library and its dependencies use:

::

    pip install ecashaddress

Usage examples
==============

As a library
------------

The first thing you need to do is import the library via:

.. code:: python

    from ecashaddress import convert
    from ecashaddress.convert import Address

Converting address
~~~~~~~~~~~~~~~~~~

**It does not matter if you use legacy or cashaddress as input.**

Then you can convert your address via:

.. code:: python

    address = Address.from_string("155fzsEBHy9Ri2bMQ8uuuR3tv1YzcDywd4").to_cash_address()

or

.. code:: python

    address = Address.from_string("ecash:qqkv9wr69ry2p9l53lxp635va4h86wv435ugq9umvq").to_legacy_address()

You can convert between different *CashAddr* prefixes:

.. code:: python

    address = Address.from_string("ecash:qqkv9wr69ry2p9l53lxp635va4h86wv435ugq9umvq").to_cash_address(prefix="foobar")

Validating address
~~~~~~~~~~~~~~~~~~

You can also validate address via:

.. code:: python

    convert.is_valid('155fzsEBHy9Ri2bMQ8uuuR3tv1YzcDywd4')

or

.. code:: python

    convert.is_valid('ecash:qqkv9wr69ry2p9l53lxp635va4h86wv435ugq9umvq')

Guessing a prefix
~~~~~~~~~~~~~~~~~

You can guess the prefix for a cash address. This only works for a short list of
commonly used prefixes, such as "ecash", "bitcoincash", "simpleledger" or "etoken".

.. code:: python

    convert.guess_prefix('qqkv9wr69ry2p9l53lxp635va4h86wv435ugq9umvq')

As a command line tool
----------------------

When the library is installed with ``pip install ecashaddress``, a
command line tool is also installed. It should normally be installed in
a location that is on your PATH, so you can run it from anywhere in a
console:

::

    ecashaddress --help

If this is not the case, an alternative is to run the library the
following way:

::

    python -m ecashaddress --help

This tool lets you convert one or more addresses to **eCash** addresses.
It accepts as input addresses with legacy BTC format, or any valid
*CashAddr*. By default, it outputs *CashAddr* with the ``ecash:``
prefix.

::

    ecashaddress convert bitcoincash:qq3dmep4sj4u5nt8v2qaa3ea7kh7km8j05dhde02hg

To output a *CashAddr* with a different prefix, use the ``--prefix``
option:

::

    ecashaddress convert bchtest:qq3dmep4sj4u5nt8v2qaa3ea7kh7km8j05f9f7das5 --prefix ectest

The tool also lets you guess the prefix from an address without prefix, if the
prefix is in a short list of commonly used prefixes:

::

    ecashaddress guessprefix qr4pqy6q4cy2d50zpaek57nnrja7289fksp38mkrxf

Development
===========

1. Fork the repository on github.
2. Clone your fork of the repository.
3. Add the source repository as a remote.

   ::

       git remote add upstream git@github.com:PiRK/ecashaddress.git
       git fetch upstream

4. Make sure your master branch is up-to-date with the upstream master.

   ::

       git checkout master
       git pull upstream master

5. Create a local development branch, and add commits to it. Run the
   tests after each change, before ``git commit``.

   ::

       git checkout -b my_dev_branch
       # do your stuff
       python -m ecashaddress.tests.test
       git commit

6. Push you branch to your fork of the repository.

   ::

       git push --set-upstream origin my_dev_branch

7. Create a pull request to the upstream repository.

