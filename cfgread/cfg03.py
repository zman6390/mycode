#!/usr/bin/env python3

#create file object in "r"ead mode

with open("vlanconfig.cfg", "r") as configfile:
    # readline() creates a lsit by reading a target
    #file line by line

    configlist = configfile.readlines()

    #file was just auto closed (no more indenting)

    #each item of the list now has the "\n" characters back

    print(configlist)
