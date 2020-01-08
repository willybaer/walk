#!/usr/bin/env python
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='walk',
    version='0.3.0',
    author='Wilhelm Dewald',
    description='PostgreSQL and MySQL. Database migration and seeds tool for postgres and mysql by using psycopg2 and mysql-connector with python3.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/willybaer/walk',
    packages=setuptools.find_packages(),
    install_requires=[
        'psycopg2',
        'mysql-connector-python'
        ],
    entry_points={
        'console_scripts': [
            'walk=walk.walk:main'
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
