#!/bin/python

import sys

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " int int") 
    exit()

intVar1 = sys.argv[1]
intVar2 = sys.argv[2]

print("The sum of " + intVar1 + " and " + intVar2 + " is " + 
  str( int(intVar1) + int(intVar2) ) )


