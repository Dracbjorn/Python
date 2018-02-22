#!/usr/bin/python
import os

def mkdir(path):
    os.mkdir(path)

def mkfile(path):
    os.mknod(path)

def write(path, string):
    f = open(path,'w')
    f.write(string)
    f.close
