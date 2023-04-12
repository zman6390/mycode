#!/usr/bin/env python3

import shutil
import os

# Forces program to run wherever we want
os.chdir("/home/student/mycode/")
# copy file at source to file destination
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#shutil.copytree() will copy an entire folder
shutil.copytree("5g_research/", "5g_research_backup/") #this will create a new folder named 5g_research_backup



