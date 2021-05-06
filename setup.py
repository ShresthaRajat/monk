#!/usr/bin/env python

"""The setup script for mazer."""

from setuptools import setup, find_packages
import os
from glob import glob

# os.system('bash install.sh')


requirements = ['flask==1.1.1',
                'flask_cors==3.0.9',
                'graphene==2.1.8',
                'flask_graphql==2.0.1',
                'turtleplus==0.1',
                'svgwrite==1.4',
                'pymongo==3.10.1',
                'bcrypt==3.1.7',
                'python-dotenv==0.13.0',
                'dnspython==1.16.0'
                ]

test_requirements = ['pytest==5.4.1',
                     'pytest-cov==2.8.1',
                     'flake8==3.7.1']

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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Hosting API",
    install_requires=requirements,
    include_package_data=True,
    keywords='fleet_management',
    name='mazer',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0]
                for path in glob('src/*.py')],
    test_suite='tests',
    tests_require=test_requirements,
    url="https://github.com/ShresthaRajat/mazer",
    version='0.1.0',
    zip_safe=True,
)
