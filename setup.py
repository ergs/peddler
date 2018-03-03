#!/usr/bin/env python
from distutils.core import setup


VERSION = '0.0.1'
setup_kwargs = {
    "version": VERSION,
    "description": 'Transport model for Cyclus',
    "author": 'Robert Flanagan, Anthony Scopatz',
    }

if __name__ == '__main__':
    setup(
        name='peddler',
        packages=["peddler"],
        **setup_kwargs
        )
