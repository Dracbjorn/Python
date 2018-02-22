#!/usr/bin/python
import sys, time, subprocess, os

filePath=sys.argv[1]

def readFile(path):
    fileOpen=open(path)
    fileContents=fileOpen.readlines()
    fileOpen.close()
    return fileContents

def copyFile(path, stringList):
    #os.mknod(path)
    newFile=open(path,'a')
   
    for line in stringList:
        newFile.write(line)

    newFile.close()

    return newFile

def filePerms(fileObject,perms,uid,gid):
    path=fileObject.name
    os.chmod(path,perms)
    os.chown(path,uid,gid)
    
def newUser(username):
    output=subprocess.check_output(['useradd', username])
    return output

fileContents=readFile(filePath)

pathToCopy=raw_input("What path would you like to copy the contents to? ")
newFile=copyFile(pathToCopy, fileContents)

username=raw_input("What user would you like to add? ")
newUser(username)

time.sleep(1)

uid=subprocess.check_output(['id', '-u', username])
gid=subprocess.check_output(['id', '-g', username])

filePerms(newFile,0440,int(uid),int(gid))

fileContents=readFile(pathToCopy)
for line in fileContents:
    print(line)

lsOutput=subprocess.check_output(['ls','-l',pathToCopy])
print(lsOutput)
