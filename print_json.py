#!/usr/bin/env python
import json
import os
from colorama import Fore, Style

path = os.getcwd() + "/json_files/"
json_files = [
    path + f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
]

for file_name in json_files:
    with open(file_name) as fil:
        json_data = json.load(fil)
        for key in json_data["Vehicle"]:
            print(
                f'{Fore.GREEN}{key}{Style.RESET_ALL}: {Fore.BLUE}{json_data["Vehicle"][key]}{Style.RESET_ALL}'
            )

print("Done!")
