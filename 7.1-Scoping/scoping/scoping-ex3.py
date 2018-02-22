#!/usr/bin/python

var="global"
def outer():
    def length(var):
        num=0
        for i in var:
            num += 1
        return num
    var="local"
    def inner():
        var=" variable"
        return var
    i=inner()
    var += i
    print("var is a "+var+" and has a length of "+str(length(var)))
outer()
