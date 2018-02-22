#!/usr/bin/python
import sys

string=sys.argv[1]

#string[[start]:stop[:step]]

def sliceString(string):

    str1=string[:3]+string[-3:]    

    str2=string[:-3]
    str2=str2[3:]

    return str1,str2

def strUpCase(string):
    return string.upper()

def reverseStr(string):
    return string[::-1]

str1,str2=sliceString(string)

strTuple=sliceString(string)
str1=strTuple[0]
str2=strTuple[1]

str1=strUpCase(str1)
str2=strUpCase(str2)

str1=reverseStr(str1)

string=str2+" "+str1

print(string)
