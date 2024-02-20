#!/bin/bash

# Build image application
#docker build -t app:1.0 .
#docker build -t app:$1 .
docker build -t rogermz/api_cdk_ene24:$1 .

echo "construido!!!"

