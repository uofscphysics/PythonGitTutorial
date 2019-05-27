#!/usr/bin/env python
import json
import os


path = os.getcwd() + "/json_files/"
json_files = [
    path + f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
]

for file_name in json_files:
    with open(file_name) as fil:
        print(json.load(fil))
