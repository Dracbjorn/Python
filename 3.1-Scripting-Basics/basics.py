#!/usr/bin/python

import sys

string = sys.argv[1]

try:
  firstname = raw_input("Enter firstname: ")
  lastname = raw_input("Enter lastname: ")
  age = int(raw_input("Enter age: "))
  sex = raw_input("Enter your sex: ")
  fullname = firstname + " " + lastname

  print2x()
except:
  firstname = input("Enter firstname: ")
  lastname = input("Enter lastname: ")
  age = int(input("Enter age: "))
  sex = input("Enter your sex: ")
  fullname = firstname + " " + lastname

  print3x()

def print2x():

  print(fullname + " is a " + str(age) + " year old " + sex + 
    " and likes to argue with the command line about " + string)

  print("%s is a %d year old %s and likes to argue with the command line about %s" % (fullname, age, sex, string) )

  print("{} is a {} year old {} and likes to argue with the command line about {}".format(fullname, age, sex, string) )

  print fullname, "is a" , age, "year old", sex, "and likes to argue with the command line about", string

def print3x():

  print(fullname + " is a " + str(age) + " year old " + sex + 
    " and likes to argue with the command line about " + string)

  print("%s is a %d year old %s and likes to argue with the command line about %s" % (fullname, age, sex, string) )

  print("{} is a {} year old {} and likes to argue with the command line about {}".format(fullname, age, sex, string) )

  print(fullname, "is a" , age, "year old", sex, "and likes to argue with the command line about", string)
