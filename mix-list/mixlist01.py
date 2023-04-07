#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]
#This line prints the first item in the list at index 0
print("The first item in the list (IP): " + my_list[0])
#This line prints the second item in the list at index 1
print("The first item in the list (port): " + str( my_list[1]))
#This line prints the third item in the list at index2
print("The first item in the list (state): " + my_list[2])

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print(iplist[3], iplist[4])
