#!/bin/python3
import requests
import json

API_URL = 'http://0.0.0.0:3001/saludo/RogerMZ'

# Test GET request
response = requests.request("GET", API_URL)

print(response.status_code)
print(response.text)

if response.status_code != 200:
    print('Se activo un fail')
    exit(1)

