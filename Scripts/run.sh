#!/bin/bash

# Stop & Delete container if exists
docker stop test_api01 || true

# Run container application
#docker run -itd --name test_api01 -p 3001:3000 --rm app:1.0 
#docker run -itd --name test_api01 -p 3001:3000 --rm app:$1
docker run -itd --name test_api01 -p 3001:3000 --rm mmedel2024/session4:$1

