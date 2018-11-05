#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='rego',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_login',
        'flask_bootstrap',
        'flask_wtf',
        'pytest',
        'coverage'
    ],
)
