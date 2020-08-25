
#! /usr/bin/env python3

import os
from PIL import Image

files = os.listdir("supplier-data/images/")

base_dir = "supplier-data/images/"

for f in files:
    if 'README' in f or 'LICENSE' in f:
        continue
    print(f)
    im = Image.open(base_dir + f)
    new_im = im.convert("RGB").resize((600, 400)).save(base_dir + f.split(".")[0]+ ".jpeg" , "JPEG")


