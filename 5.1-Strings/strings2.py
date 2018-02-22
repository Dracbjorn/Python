#!/bin/python

import sys

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " string")
    exit()

string = sys.argv[1]

def sliceString(string):
    if len(string) < 7:
        print("String must be at least 7 characters long")
        exit()

    str1 = string[:3] + string[-3:]
    str2 = string[3:-3]

    return str1, str2

def strUpcase(string):
    return string.upper()

def reverseStr(string):
    return string[::-1]
    
str1, str2 = sliceString(string)

str1 = strUpcase(str1)
str2 = strUpcase(str2)

str1 = reverseStr(str1)

string = str2 + " " + str1

print(string)
