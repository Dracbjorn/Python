#!/bin/python

import sys

if len(sys.argv) == 3:
    arg1=sys.argv[1]
    arg2=sys.argv[2]
    print("First Name="+arg1+",Last Name="+arg2)
elif len(sys.argv) > 3:
    print("No more than 2 arguments")
    exit()
else:
    print("Usage: "+sys.argv[0]+" FirstName LastName")
