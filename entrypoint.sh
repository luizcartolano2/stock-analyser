#!/bin/bash
exec gunicorn --config gunicorn_config.py src.app:app
