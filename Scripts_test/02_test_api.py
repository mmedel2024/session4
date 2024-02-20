#!/bin/python3
import requests
import json

API_URL = 'http://0.0.0.0:3001/convertir'

payload = json.dumps({
    "numero": 42,
    "base_actual": 10,
    "base_deseada": 2
})

headers = { 'Content-Type': 'application/json' }

# Test GET request
response = requests.request("POST", API_URL, headers=headers, data=payload)

print(response.status_code)
print(response.text)

if response.status_code != 200:
    print('Se activo un fail')
    exit(1)

