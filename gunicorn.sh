#!/usr/bin/sh

source .venv/bin/activate

gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 192.168.1.101:9999 "application.wsgi" --reload --threads 2