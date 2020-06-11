#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages


setup(name='tkbuilder',
      version='0.1.0',
      description='Tools for building GUI interfaces in Tkinter',
      author='NGA',
      author_email='j.casey@beamio.net',
      include_package_data=True,
      packages=find_packages(),
      install_requires=[
              'pillow',
              'numpy',
              'matplotlib',
          ],
      )
