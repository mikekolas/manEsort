#!/bin/python
#
#######################################################################################
# Written by mikekolas                                                                #
# Optional script to run, depending of the names of your .jpg's.                      #
# See README.txt for information about this script.                                   #
# This python script must be in the same folder as the images you want to sort.       #
#######################################################################################
import os,sys

path = '.'
num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
num_files -= 1 #the script is counted also so we must remove it
for i in range(0,num_files):
    if(i<10):
        os.rename("00" + str(i) + ".jpg", str(i) + ".jpg")
    else:
        os.rename("0" + str(i) + ".jpg", str(i) + ".jpg")
