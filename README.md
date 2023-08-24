# Mazer

A simple and artistic maze generator!

[![license](https://img.shields.io/badge/license-MPL%202.0-important)](LICENSE)

[![Tagged Release](https://img.shields.io/badge/release-v1.0.0-blue.svg?longCache=true)](CHANGELOG.md)

[![codecov](https://codecov.io/gh/ShresthaRajat/mazer/branch/master/graph/badge.svg?token=TQYCIP62MZ)](https://codecov.io/gh/ShresthaRajat/mazer)

![Docker](https://github.com/ShresthaRajat/mazer/workflows/Docker/badge.svg?branch=master)


## Requirements
Docker, Dockercompose

## Getting Started
Create a .env file with mongo key, flask secret key, and flask debug status

```
MONGO_MAZER_KEY="MONGO CONNECTION STRING"
SECRET_KEY="SECRET KEY"
DEBUG=True/False
```
Run
```
docker-compose up -d
```
