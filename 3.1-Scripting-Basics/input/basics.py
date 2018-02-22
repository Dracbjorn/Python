#!/usr/bin/python

import sys

string=sys.argv[1]

firstname=raw_input("Enter firstname: ")
lastname=raw_input("Enter lastname: ")
age=int(raw_input("Enter age: "))
sex=raw_input("Enter your sex: ")

fullname=firstname+" "+lastname

print(fullname+" is a "+age+" year old "+sex+" and likes to argue with the command line about "+string)
