#!/bin/bash
python ./lib/gunicorn/__main__.py wsgi:application -b 0.0.0.0:8000