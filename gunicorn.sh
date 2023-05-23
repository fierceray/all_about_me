#!/bin/bash
./venv/bin/gunicorn wsgi:application -b 0.0.0.0:8000