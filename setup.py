#!/usr/bin/env python
from os.path import dirname, join
from setuptools import setup


setup(
    name='optimus-manager',
    version='0.0.1',
    description='Management utility for Optimus laptops on Linux.',
    long_description=open(
        join(dirname(__file__), 'README.md')).read(),
    url='https://github.com/Askannz/optimus-manager',
    author='Robin Lange',
    author_email='robin.langenc@gmail.com',
    license='MIT',
    packages=['optimus_manager'],
    entry_points={
        'console_scripts': [
            'optimus-manager=optimus_manager.optimus_manager:main',
            'optimus-manager-daemon=optimus_manager.optimus_manager_daemon:main',
        ],
    },
    keywords=['optimus', 'nvidia', 'bbswitch', 'prime', 'gpu'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
