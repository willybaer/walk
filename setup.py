#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='walk',
    version='0.2',
    author='Wilhelm Dewald',
    description='My own database migration and seeds tool for postgres by using psycopg2 with python3.',
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
