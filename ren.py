#!/bin/python
#optional script to run, depending of the names of your .jpg's
import os,sys

path = '.'
num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))

for i in range(0,num_files):
    if(i<10):
        os.rename("00" + str(i) + ".jpg", str(i) + ".jpg")
    else:
        os.rename("0" + str(i) + ".jpg", str(i) + ".jpg")
