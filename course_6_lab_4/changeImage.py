#!/usr/bin/env python3

import os
from PIL import Image

dir_path = os.path.expanduser('~') + '/supplier-data/images/'
for image in os.listdir(dir_path):
    f, e = os.path.splitext(image)
    imageJPEG = f + ".jpeg"
    try:
        with Image.open(dir_path + image) as im:
            im_jpeg = im.convert("RGB").resize((600, 400)).save(dir_path + imageJPEG, 'JPEG')
    except OSError:
        print("cannot convert " + image)
