#!bin/python
#######################################################################################
# Written by mikekolas                                                                #
#                                                                                     #
# This python script must be in the same folder as the images you want to sort        #
#######################################################################################
import os, sys

path = '.'
num_files = sum(os.path.isfile(os.path.join(path, f)) for f in os.listdir(path))
num_files -= 1 #we remove one file because the script counts it self
times = num_files / 4
ch1 = 1 #makes the 2nd page 3rd for the printing
ch2 = 3 #makes the 4th page 2nd for the printing, thus the new 3rd 4th

mod = num_files % 4
if(mod == 0): # Depending on the value mod has, you always know how many files are not renamed,
            #thus the script creates as many files as are neccesary to be 4 in total.
    for i in range(0,times + 1):  #the format of the new name is "newpage"_"oldPage".jpg
        os.rename(str(ch1) + ".jpg", str(ch1 + 1) + "_" + str(ch1) + ".jpg")
        os.rename(str(ch2) + ".jpg", str(ch2 - 3) + "_" + str(ch2) + ".jpg")
        ch1 += 4
        ch2 += 4
elif(mod == 1): #if mod=1 then times *.25
    times = times - 0.25
    for i in range(0,int(times + 1)):  #the format of the new name is "newpage"_"oldPage".jpg
        os.rename(str(ch1) + ".jpg", str(ch1 + 1) + "_" + str(ch1) + ".jpg")
        os.rename(str(ch2) + ".jpg", str(ch2 - 3) + "_" + str(ch2) + ".jpg")
        ch1 += 4
        ch2 += 4
    for j in range(ch1,ch1 + 3):
        os.mknod(str(j) + ".jpg")
    #The last 4 files are renamed here
    os.rename(str(ch1) + ".jpg", str(ch1 + 1) + "_" + str(ch1) + ".jpg")
    os.rename(str(ch2) + ".jpg", str(ch2 - 3) + "_" + str(ch2) + ".jpg")
elif(mod == 2): #if mod=1 then times *.50
    times = times - 0.50
    for i in range(0,int(times + 1)):  #the format of the new name is "newpage"_"oldPage".jpg
        os.rename(str(ch1) + ".jpg", str(ch1 + 1) + "_" + str(ch1) + ".jpg")
        os.rename(str(ch2) + ".jpg", str(ch2 - 3) + "_" + str(ch2) + ".jpg")
        ch1 += 4
        ch2 += 4
    for j in range(ch1 + 1,ch1 + 3):
        os.mknod(str(j) + ".jpg")
    #The last 4 files are renamed here
    os.rename(str(ch1) + ".jpg", str(ch1 + 1) + "_" + str(ch1) + ".jpg")
    os.rename(str(ch2) + ".jpg", str(ch2 - 3) + "_" + str(ch2) + ".jpg")
else:   #if mod=3 then times *.75
    times = times - 0.75
    for i in range(0,int(times + 1)):  #the format of the new name is "newpage"_"oldPage".jpg
        os.rename(str(ch1) + ".jpg", str(ch1 + 1) + "_" + str(ch1) + ".jpg")
        os.rename(str(ch2) + ".jpg", str(ch2 - 3) + "_" + str(ch2) + ".jpg")
        ch1 += 4
        ch2 += 4
    j = ch1 + 2
    os.mknod(str(j) + ".jpg") #creates the last jpg to make it 4 in total
    #The last 4 files are renamed here
    os.rename(str(ch1) + ".jpg", str(ch1 + 1) + "_" + str(ch1) + ".jpg")
    os.rename(str(ch2) + ".jpg", str(ch2 - 3) + "_" + str(ch2) + ".jpg")
