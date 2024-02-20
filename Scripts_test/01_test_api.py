#!/bin/python3
import requests
import json

API_URL = 'http://0.0.0.0:3001/rlineal'

payload = json.dumps({
    "vx": [2014, 2015, 2016, 2017, 2018, 2019],
    "vy": [530, 560, 610, 690, 720, 830],
    "x": 2020
})

headers = { 'Content-Type': 'application/json' }

# Test GET request
response = requests.request("POST", API_URL, headers=headers, data=payload)

print(response.status_code)
print(response.text)

if response.status_code != 200:
    print('Se activo un fail')
    exit(1)

