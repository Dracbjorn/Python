#!/bin/python
import socket, subprocess, sys, time, os
client = socket.socket()
client.connect(('172.16.28.135', 1337))
while True:
    cmd_data = raw_input("# ")
    if cmd_data.find('exit') >= 0:
        break
        client.close()
    else:
        client.sendall(cmd_data)
    while True:
        data = client.recv(1024)
        print(data)
        if len(data) < 1024:
            break
