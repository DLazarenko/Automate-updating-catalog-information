#!/usr/bin/env python3

import os
import requests

path = os.path.expanduser('~') + '/supplier-data/descriptions/'
for txt_file in os.listdir(path):
    f, e = os.path.splitext(txt_file)
    if e == ".txt":
        fb = open(path + txt_file)
        linesList = fb.readlines()
        # explicit conversion from string to int
        weight_int = int(''.join(filter(str.isdigit, linesList[1])))
        dictionary = {'name': linesList[0], 'weight': weight_int,
                      'description': linesList[2], 'image_name': f + ".jpeg"}
        # where <35.239.184.74> - linux-instance-external-IP
        response = requests.post("http://35.239.184.74/fruits/", json=dictionary)
