#!/bin/bash

cd /workspace

setsid nohup gunicorn src.application:app --error-logfile logs/error.log --access-logfile logs/access.log -b 0.0.0.0:8787 -w 4 -k uvicorn.workers.UvicornWorker
