#!/usr/bin/sh

source .venv/bin/activate

gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 127.0.0.1:9999 "application.wsgi" --reload --threads 2