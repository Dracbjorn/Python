#!/bin/python

from pdb import set_trace as bp

def hello():
    for i in range(1,3):
        bp()
        print("Hello World")

def main():
    hello()
