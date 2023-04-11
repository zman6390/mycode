#!/usr/bin/env python3
import random

def main():
    my_list = [ "192.168.0.5", 5060, "UP" ]
    #This line prints the first item in the list at index 0
    print("The first item in the list (IP): " + my_list[0])
    #This line prints the second item in the list at index 1
    print("The first item in the list (port): " + str( my_list[1]))
    #This line prints the third item in the list at index2
    print("The first item in the list (state): " + my_list[2])

    iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

    print(iplist[3], iplist[4])

    wordbank = ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    wordbank.append(4)

    #num = int(input("Pick a number between  0 and 20!\n"))
    #bonus 1
    #num = random.randint(0,20)
    #bonus 2
    num = int(input(f"Pick a number between 1 and {len(tlgstudents)}\n"))-1
    student_name = tlgstudents[num]

    print(student_name, "always uses", wordbank[2], wordbank[1], "to indent.")

if __name__ == "__main__":
    main()
