#!/bin/sh

export FLASK_APP=./product-listing-module/index.py
export FLASK_DEBUG=1

source $(pipenv --venv)/bin/activate

flask run -h 0.0.0.0