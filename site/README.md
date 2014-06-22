# bootctf site #

The BootCTF site tracks users and challenges for the internal CCoWMU CTF.

## Overview ##

The site is a [Flask](http://flask.pocoo.org/docs/) site written in Python3.4
and will probably use a SQL database for persistent storage.

The changes in the 3.X series of python releases are rather minor, but if you
are coming from Python 2.X, there are a few changes to be aware of; most of
them are noted [here](https://docs.python.org/3/whatsnew/3.0.html).

## Hacking ##

Work in a feature branch and then send a pull request on `master`.

    $ git checkout -b rad-work
    $ # work and commit here
    $ git push origin rad-work:
    $ # send github pull request from rad-work to master here

You will probably want to work in a Python3.4 venv. The `gitignore` currently
includes an entry for `venv`, so make sure you name yours to match:

    $ cd bootctf/site/
    $ pyvenv-3.4 venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt
