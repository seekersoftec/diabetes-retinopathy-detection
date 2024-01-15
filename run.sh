#!/usr/bin/env bash

source ./env/bin/activate

uvicorn "manage:app" "--host" "0.0.0.0" "--port" "8000" --reload