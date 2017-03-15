#!/usr/bin/env python
import os.path
from setuptools import setup

import jproperties


README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Internationalization",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Java Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="jproperties3",
    py_modules=["jproperties"],
    author=jproperties.__author__,
    author_email=jproperties.__email__,
    classifiers=CLASSIFIERS,
    description="Python library for Java .properties file parsing",
    download_url="https://github.com/Leibniz137/python-jproperties3/tarball/master",
    long_description=README,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url="https://github.com/Leibniz137/python-jproperties3",
    version=jproperties.__version__,
)
