#!/usr/bin/python

a=2
print(a-2)
def function1(a):
    a -= 1
    print(a)
def function2(a):
    print(a)
    a += 2
    return a
def function3(a):
    a -= 1
    print(a)
    def function4():
        global a
        print(a)
    function4()
function1(a)
a=function2(a)
function3(a)
a += 1
print(a)
