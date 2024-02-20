#!/bin/bash

# Build image application
#docker build -t app:1.0 .
#docker build -t app:$1 .
docker build -t mmedel2024/session4:$1 .

echo "construido!!!"

