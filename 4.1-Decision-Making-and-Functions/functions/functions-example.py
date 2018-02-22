#!/usr/bin/python

main(hello(goodbye()))

def hello(string):
    var="Well hello there!"
    return var + " " + string

def goodbye():
    var="Goodbye my friend!"
    return var

def main(string):
    print(string)


