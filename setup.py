#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import os
from glob import glob

# os.system('bash install.sh')

requirements = ['turtleplus', 'graphene']

test_requirements = ['pytest>=3', ]

setup(
    author="Rajat Shestha",
    author_email='rajat.shrestha@eydean.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Alpha',
        'Intended Audience :: Editors',
        """License :: OSI Approved ::
        Mozilla Public License Version 2.0 (GPLv3)""",
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Hosting API",
    install_requires=requirements,
    include_package_data=True,
    keywords='fleet_management',
    name='maizer',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0]
                for path in glob('src/*.py')],
    test_suite='tests',
    tests_require=test_requirements,
    url="https://github.com/ShresthaRajat/maizer",
    version='0.1.0',
    zip_safe=True,
)
