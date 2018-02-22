#!/usr/bin/python

from subprocess import *

stdout, stderr = Popen(["find", "/proc"], stderr=PIPE, stdout=PIPE).communicate()
print(stdout)
print(stderr)

#output = Popen(["find", "/proc"], stdout=PIPE, stderr=PIPE)
#
#output = output.communicate()
#
#stdout=output[0]
#
#stderr=output[1]
#
#print("=========================")
#print(stdout)
#print("=========================")
#print(stderr)
