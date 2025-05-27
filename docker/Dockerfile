FROM python:3.13-alpine

RUN apk add --no-cache \
        gettext \
        gettext-dev \
        alpine-sdk

RUN pip install --no-cache-dir watchdog

WORKDIR /app

COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY translations /app/translations

RUN pybabel compile -d translations

COPY . .
