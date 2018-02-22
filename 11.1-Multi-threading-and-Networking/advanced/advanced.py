#!/bin/python

import sys, socket, threading

if len(sys.argv) == 2:
    remoteHostsFilePath = sys.argv[1]
else:
    print("Usage: {} filename".format(sys.argv[0]))
    sys.exit()

remoteHostsFile = open(remoteHostsFilePath)
remoteHosts = remoteHostsFile.readlines()

socket.setdefaulttimeout(.001)

class NewThread(threading.Thread):
    def __init__(self,ip):
        self.ip = ip
        threading.Thread.__init__(self)
    def run(self):
        scan(self.ip)

def scan(ip):
    print("Scanning {}...".format(ip))
    outFile = "{}.txt".format(ip)
    outFile = open(outFile,'w')
    for port in range(1,1025):
        s = socket.socket()
        result = s.connect_ex((ip,port))
        if result == 0:
            results="{}:{} OPEN".format(ip,port)
            outFile.write(results+'\n')
        s.close()
    outFile.close()

#threadLock = threading.Lock()

for ip in remoteHosts:
    ip=ip.rstrip()
    thread = NewThread(ip)
    thread.start()

while len(threading.enumerate()) > 1:
    pass

#Additional code
for ip in remoteHosts:
    ip=ip.rstrip()
    outFile="{}.txt".format(ip)
    #outFile=open(outFile,"r")
    #outFile=outFile.readlines()
    for line in open(outFile,"r").readlines():
        print(line.rstrip())
    print("===============")
