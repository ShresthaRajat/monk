# mazer

[![GitHub](https://img.shields.io/badge/developer-ShresthaRajat-black)](AUTHORS.md)
[![license](https://img.shields.io/badge/license-MPL%202.0-important)](LICENSE)

[![Tagged Release](https://img.shields.io/badge/release-v1.0.0-blue.svg?longCache=true)](CHANGELOG.md)
[![Development Status](https://img.shields.io/badge/status-stable-blue.svg?longCache=true)](ROADMAP.md)

[![build Status](https://travis-ci.com/ShresthaRajat/mazer.svg?token=vfBmyikLTqJ4tJUVico1&branch=master)](https://travis-ci.com/ShresthaRajat/mazer)
[![codecov](https://codecov.io/gh/ShresthaRajat/mazer/branch/master/graph/badge.svg?token=TQYCIP62MZ)](https://codecov.io/gh/ShresthaRajat/mazer)
[![Heroku App Status](http://heroku-shields.herokuapp.com/maze-r)](https://maze-r.herokuapp.com)

[![Python package](https://github.com/ShresthaRajat/mazer/workflows/Python%20package/badge.svg?branch=master)](https://github.com/ShresthaRajat/mazer/actions?query=workflow%3A%22Python+package%22)
[![Python application](https://github.com/ShresthaRajat/mazer/workflows/Python%20application/badge.svg?branch=master)](https://github.com/ShresthaRajat/mazer/actions?query=workflow%3A%22Python+application%22)
[![Docker Image CI](https://github.com/ShresthaRajat/mazer/workflows/Docker%20Image%20CI/badge.svg?branch=master)](https://github.com/ShresthaRajat/mazer/actions?query=workflow%3A%22Docker+Image+CI%22)
![Docker](https://github.com/ShresthaRajat/mazer/workflows/Docker/badge.svg?branch=master)




mazer and the maze generator.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Developer Guide](#developer-guide)
- [Docker Packages](#docker-packages)
- [Development](#development)
  - [Future](#future)
  - [Community](#community)

## Features
This Project can host a simple platform for a maze generator and provides an Endpoint which provides the required information to generate a maze.

## Requirements
Python 3.5 or higher for the maze generator to work. The required python packages are:
- flask
- flask_cors
- graphene
- flask_graphql
- turtleplus
- pytest
- pytest-cov
- flake8
- svgwrite
- gunicorn
- bcrypt
- python-dotenv
- pymongo
- dnspython
  
Test Requirements:
- pytest
- pytest-cov
- flake8

> Note: These packages will be auto installed during the setup

For ease of use the whole package to host the API is contenarized in docker so the following are recommended but not necessary:
- Docker
- Docker-compose

## Developer Guide

Step 1: Clone this repo:

```
git clone https://github.com/ShresthaRajat/mazer.git

cd mazer
```


Step 2: Create a .env file with mongo key, flask secret key, and flask debug status

```
MONGO_MAZER_KEY="connection string for python 3.6 or greater"
SECRET_KEY="your secret key"
DEBUG=True/False

```

Step 3: Install the python module and run app.py

```
pip install -e .

python -m app
```


Alternative: If you have docker and docker-compose simply run

```
docker-compose up --build
```

## Docker Packages

You can simply run the following command if you have docker installed:
```
sudo docker run -p 8001-8001 shrestharajat/mazer
```

Note: You have to setup connection string inside the docker container for mongo db if you also want to setup CRUD operations

## Development

See [CONTRIBUTING](CONTRIBUTING.md)

### Future

See [ROADMAP](ROADMAP.md)

### Community

See [CODE OF CONDUCT](CODE_OF_CONDUCT.md)
