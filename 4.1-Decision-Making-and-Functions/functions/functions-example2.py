#!/usr/bin/python

import sys

def hello():
    var="Well hello there!"
    return var

def goodbye():
    var="Goodbye my friend!"
    return var

def main(arg):
    
    if arg == "hi":
        var1=hello()
        print(var1)
    elif arg == "bye":
        var2=goodbye()
        print(var2)
    else:
        print("Usage: " + sys.argv[0] + " hi|bye")

main(sys.argv[1])
