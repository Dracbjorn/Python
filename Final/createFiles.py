#!/usr/bin/python

import sys, os, fileOperations

global directory
global path

if (len(sys.argv) == 2):
    directory = sys.argv[1]
else:
    print("Usage: "+sys.argv[0]+" /path")
    exit()

res = os.path.exists(directory)
if not res:
    while True:
      print(directory+" does not exist")
      ans = raw_input("Would you like to create it?[y/n] ")

      if ans == "y":
          try:
            fileOperations.mkdir(directory)
            print("Directory was created: "+directory)
          except:
            print("An error occured")
            exit()
          break
      elif ans == "n":
          exit()
      else:
          print("Invalid response")
          continue

path = directory+"/file"
for i in range(1,20+1):
    fileName = path+str(i) #name of the file
    if not os.path.exists(fileName): #check if file already exists
        fileOperations.mkfile(fileName) #create the file
        print("Created file: "+fileName)
        fileOperations.write(fileName, "file"+str(i)+": This is an exercise\n")
        print("Wrote to the file: "+fileName)
    else:
        print(fileName+": already exists!")
        continue

files = os.listdir(directory)
print("Listing contents of "+directory+":\n")
for i in files:
    curFile = open(directory+"/"+i)
    contents = curFile.readlines()
    for j in contents:
        print(j)
