#!/usr/bin/env python3
import re
import random
eyebrow_style = ["thick","thin"]
face_style = ["oblong", "oval"]  ## To replace diamond faces

with open("Train1209.txt", "r") as f:
    for line in f:
        new_line = line.replace(" up","").replace(" down","").replace("has ","has a ").replace("has an","has a").replace("ears are medium","ears are normal").replace("long nose","roman nose").replace("medium eyes","normal eyes").replace("has a a ","has a ").replace("has a an","has an").replace("large hair", "long hair").replace("has a glasses", "has glasses").replace("has a beard","has beard")
        new_line = new_line.replace("\t"," ").replace(" His",". His").replace("Her", ". Her").replace("She", ". She").replace("He", ". He").replace("moth", "mouth").replace("small hair","short hair").replace("big ears","ears are big").replace("medium ears", "ears are medium").replace("small ears", "ears are small")
        
        
        if "dense thick" not in new_line and "dense thin" not in new_line:
            new_line = new_line.replace("dense ","dense "+eyebrow_style[random.randint(0,1)]+" ")

        if "sparse thick" not in new_line and "sparse thin" not in new_line:
            new_line = new_line.replace("sparse ","sparse "+eyebrow_style[random.randint(0,1)]+" ")


        result = re.sub(r"has a [o]", "has an o", new_line)
        result = re.sub(r"has a [i]", "has an i", result)
        
        result_list = result.split()

        for i in range(0,len(result_list)):
            if (result_list[i] == "long" and "man" in result_list) or (result_list[i] == "short" and "woman" in result_list):
                result_list[i] = "medium"
            if (result_list[i] == "diamond"):
                result_list[i] =face_style[random.randint(0,1)]

        new_result = " ".join(result_list) 
        new_result = new_result.strip()
        print(new_result)