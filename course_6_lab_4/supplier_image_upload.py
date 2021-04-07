#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
dir_path = os.path.expanduser('~') + '/supplier-data/images/'
for image in os.listdir(dir_path):
    if '.jpeg' in image:
        with open(dir_path + image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
