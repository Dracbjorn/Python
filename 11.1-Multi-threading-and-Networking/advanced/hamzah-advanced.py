#!/usr/bin/python
import socket, threading, sys, os, time
from pdb import *

remoteHostsFile=sys.argv[1]
remoteHosts=open(remoteHostsFile,"r")
remoteHosts=remoteHosts.readlines()

socket.setdefaulttimeout(.001)

class newThread(threading.Thread):
  def __init__(self, ip):
    self.ip = ip
    threading.Thread.__init__(self)

  def run(self):
    threadLock.acquire()
    scan(self.ip)
    threadLock.release()
 
def scan(ip):
  try:
    print(ip)
    outFilename="./"+ip+".txt"
    f = open(outFilename, "a")
    for port in range(1, 1025):
      s = socket.socket()
      result = s.connect_ex((ip, port))
      if result == 0:
        print(ip + ":" + str(port) + " OPEN")
        f.write(str(port) + "\n")
      else:
        print(ip + ":" + str(port) + " CLOSED")
      s.close()
    f.close()
  except:
    print("error")

threadLock=threading.Lock()

for ip in remoteHosts:
  ip = ip.rstrip()
  thread = newThread(ip)
  thread.start()
  #time.sleep(1)
  
#while len(threading.enumerate()) > 1:
#  pass
