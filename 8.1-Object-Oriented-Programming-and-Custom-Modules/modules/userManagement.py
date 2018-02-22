import os
import crypt as c

def getUserName(first, middle, last):
    userName=first[0]+middle[0]+last[0:5]
    return userName

def createUser(username):
    defaultPassword=username+"2017!"
    encPassword=c.crypt(defaultPassword)
    os.system("/usr/sbin/useradd -p "+encPassword+" "+username)
