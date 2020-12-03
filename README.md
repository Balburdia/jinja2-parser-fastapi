# Jinja2 Live Parser with FastAPI :)

A lightweight live parser for Jinja2 based on FastAPI and Jquery.
Can parse JSON and YAML inputs.

This project was based on https://github.com/qn7o/jinja2-live-parser

## Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).

## Running the application

* Start it with Docker Compose:

```bash
docker-compose up -d
```

* Now you can open your browser and interact with these URLs:

Front-end page which provides live jinja2 rendering: http://localhost:8000/

Backend, JSON based web API based on OpenAPI: http://localhost:8000/api/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost:8000/docs

Alternative automatic documentation with ReDoc (from the OpenAPI backend): http://localhost:8000/redoc

To check the logs, run:

```bash
docker-compose logs
```

## Usage

You are all set, go to http://localhost:8000/ and have fun.
