#!/usr/bin/python
import sys
import socket
import threading
import time
import re
from subprocess import *

if len(sys.argv) == 3:
    HOST=sys.argv[1]
    PORT=int(sys.argv[2])
elif len(sys.argv) == 2:
    FILE=sys.argv[1]
else:
    print("Usage: "+sys.argv[0]+" <ip> "+"<port>")
    sys.exit()

class newThread(threading.Thread):

    def __init__(self, client, ip):
        self.client=client
        self.ip=ip
        self.threadLog=open('./threadlog-'+self.ip+'.txt', 'a+')
        threading.Thread.__init__(self)

    def run(self):
        self.connect()
        self.log("Closing connection")
        self.threadLog.close()

    def connect(self):
        while True:
            try:
                data = self.client.recv(1024)
                if data:
                    self.log("<- "+data)
                    pattern = re.compile("^sudo .*")
                    if re.match(pattern,data):
                        self.log("Enter sudo password: ")
                        self.client.sendall("Enter sudo password: ")
                        output = Popen(data, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
                            data = self.client.recv(1024)
                            output = output.communicate(data)
                    else:
                        output = Popen(data, shell=True, stdout=PIPE, stderr=PIPE)
                        output = output.communicate()

                    for out in output:
                        self.client.sendall(out)
                        self.log("-> "+out)
                else:
                    self.client.close()
                    break
            except socket.error, ex:
                self.log(str(ex))

    def log(self,string):
        print(self.ip+": "+string)
        timeTuple = time.localtime()[:6]
        timeStamp = ''
        for i in timeTuple:
            if len(str(i)) == 1:
                i='0'+str(i)
            timeStamp=timeStamp+str(i)
        self.threadLog.write(timeStamp+': '+string)
  
server=socket.socket()
while True:
    try:
        server.bind((HOST,PORT))
        server.listen(5)
        break
    except socket.error, ex:
        print("Error: Could not bind socket")
        print(ex)
        for i in range(3):
            print(R"Trying again in "+str(i+1)+"...")
            time.sleep(i)
        continue

while True:
    print("Listening for connection...")
    client, addr = server.accept()
    ip=addr[0]
    print("Connection accepted from "+ip)
    connection = newThread(client,ip)
    print("Starting thread for connection...")
    connection.start()
