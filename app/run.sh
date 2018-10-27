#!/bin/bash
set -e
pip install -r /project/app/requirements.txt
cd /project/app && gunicorn -b 0.0.0.0:8000 api:app