#!/bin/python

studentList = [ ['joe','smith'], ['mary','jones'], ['sally','brown'] ]

print(studentList)
for student in studentList:
    print(student)
    for name in student:
        print(name)


