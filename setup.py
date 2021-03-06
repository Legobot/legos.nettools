#!/usr/bin/env python

from setuptools import setup, find_packages

__author__ = "Nitrax <nitrax@lokisec.fr>"
__copyright__ = "Copyright 2017, Legobot"

description = 'Lego providing networking tools'
name = 'legos.nettools'
setup(
    name=name,
    version='0.1.0',
    namespace_packages=name.split('.')[:-1],
    license='MIT',
    description=description,
    author='Nitrax',
    url='https://github.com/Legobot/' + name,
    install_requires=['legobot>=1.1.4,<=2.0.0',
                      'python-whois',
                      'urllib3'
                      ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta'
    ],
    packages=find_packages()
)
