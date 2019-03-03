#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='prettyprint',
    version='0.0',

    url='https://github.com/sherry255/prettyprint',
    description='prettyprint',
    license='BSD',

    classifiers=[
        "Development Status:: 5 - Production / Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System:: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],

    author='sherry',
    author_email='xcmkya@gmail.com',

    py_modules=['prettyprint'],
    zip_safe=False,
)
