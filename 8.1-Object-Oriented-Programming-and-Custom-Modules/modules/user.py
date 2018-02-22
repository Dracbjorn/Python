#!/bin/python

import userManagement as um

first=raw_input("Enter first name: ")
middle=raw_input("Enter middle name: ")
last=raw_input("Enter last name: ")

userName=um.getUserName(first, middle, last)

um.createUser(userName)

print("User "+userName+" was created.")
