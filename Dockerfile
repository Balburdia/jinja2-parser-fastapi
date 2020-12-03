FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

# Install dependencies
RUN apt-get update && apt-get install -y curl
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -U -r requirements.txt

WORKDIR /
ENV PYTHONPATH=.
ENV APP_MODULE=app.main:app

COPY ./app /app