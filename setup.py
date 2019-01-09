#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='walk',
    version='0.0.1',
    author='Wilhelm Dewald',
    description='My own database migration tool for postgres by using psycopg2 for python3.',
    long_description_content_type='text/markdown',
    install_requires=[
        'psycopg2'
        ],
    entry_points={
        'console_scripts': [
            'walk=walk:main'
        ],
    }
)
