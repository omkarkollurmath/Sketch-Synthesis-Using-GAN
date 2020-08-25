#!/usr/bin/env python3

import codecs

with open("with_dot_caption.txt", "rb") as f:
    contents = f.read()


contents = contents.rstrip("\n").decode("utf-16")
contents = contents.split("\r\n")

print(contents)