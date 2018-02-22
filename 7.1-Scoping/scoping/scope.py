#!/bin/python

a="global"
print(a)
b="parent"

def function():
    global a
    a="local"
    print(a)
    print(b)

function()
print(a)
