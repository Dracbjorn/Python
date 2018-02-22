#!/usr/bin/python

import socket
c = socket.socket()
c.connect(('172.16.28.235',1337))
while 1:
    userInput=raw_input('# ')
    c.sendall(userInput)
    while 1:
        print(c.recv(1024))
