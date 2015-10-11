getlyrics
=========

A Python program which gets the lyrics for a song and outputs them to
stdout

Usage
-----

::

    usage: getlyrics [-h] [-i INDEX] [--startFromZero] term

    positional arguments:
      term                  Search term

    optional arguments:
      -h, --help            show this help message and exit
      -i INDEX, --index INDEX
                            Specify song index, if multiple results are returned

    Data loaded from AZLyrics.com. Used without permission. This is effectively a
    shortcut for opening a browser, but I guess it does skip loading ads.

Installation
------------

Via ``pip``:

::

    pip3 install getlyrics

Alternatively:

-  Clone the repository, ``cd getlyrics``
-  Run ``python3 setup.py install`` or ``pip3 install -e``
