# mazer

[![GitHub](https://img.shields.io/badge/developer-ShresthaRajat-black)](AUTHORS.md)

[![Tagged Release](https://img.shields.io/badge/release-v0.2.0-blue.svg?longCache=true)](CHANGELOG.md)
[![license](https://img.shields.io/badge/license-MPL%202.0-important)](LICENSE)
[![Development Status](https://img.shields.io/badge/status-alpha-yellow.svg?longCache=true)](ROADMAP.md)

[![build Status](https://travis-ci.com/ShresthaRajat/mazer.svg?token=vfBmyikLTqJ4tJUVico1&branch=master)](https://travis-ci.com/ShresthaRajat/mazer)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FShresthaRajat%2Fmazer%2Fbadge%3Fref%3Dmaster%26token%3D759aeafb52f9ee9c6684bfc28abf7b54bcb521b3&style=flat)](https://actions-badge.atrox.dev/ShresthaRajat/mazer/goto?ref=master&token=759aeafb52f9ee9c6684bfc28abf7b54bcb521b3)

![Python package](https://github.com/ShresthaRajat/mazer/workflows/Python%20package/badge.svg?branch=master)
![Python application](https://github.com/ShresthaRajat/mazer/workflows/Python%20application/badge.svg?branch=master)

[![codecov](https://codecov.io/gh/ShresthaRajat/mazer/branch/master/graph/badge.svg?token=TQYCIP62MZ)](https://codecov.io/gh/ShresthaRajat/mazer)

maze generetor for maze master project

_**Note:** This project was initially created by [cookiecutter-git](https://github.com/NathanUrwin/cookiecutter-git)!_ :cookie:

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
  - [Future](#future)
  - [History](#history)
  - [Community](#community)
- [Credits](#credits)
- [License](#license)

## Features
This Project can host a simple platform for a maze generetor and provides an Endpoint which provides the required information to generate a maze.

## Requirements
Python 3.5 or higher for the maze generetor to work. The required python packages are:
- flask
- flask_cors
- graphene
- flask_graphql
- turtleplus
- pytest
- pytest-cov
- flake8
- svgwrite

> Note: These packages will be auto installed during the setup

The Server will be hosted 

For ease of use the whole package to host the API is contenarized in docker so the following are recommended but not necessary:
- Docker
- Docker-compose

## Installation

Clone this repo and run:

```
git clone https://github.com/ShresthaRajat/maizer.git

cd maizer

pip install -e .
```

you can skip this step if you want to use docker (docker-compose insted)

With docker and docker-compose installed run this on the maizer directory:

```
docker-compose up --build
```

## Usage:

To run the GraphQL server you can run the following command

```
python -m src.graphql_server
```


## Development

See [CONTRIBUTING](CONTRIBUTING.md)

### Future

See [ROADMAP](ROADMAP.md)

### History

See [CHANGELOG](CHANGELOG.md)

### Community

See [CODE OF CONDUCT](CODE_OF_CONDUCT.md)
