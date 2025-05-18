FROM python:3.12-alpine

RUN apk add --no-cache \
        gettext \
        gettext-dev \
        alpine-sdk

WORKDIR /app

COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pybabel compile -d translations