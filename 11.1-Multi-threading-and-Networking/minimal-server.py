#!/usr/bin/python
import socket, subprocess, time
server = socket.socket()
server.bind(('127.0.0.1', 12345))
server.listen(5)
while True:
    client = server.accept()[0]
    while True:
        cmd = client.recv(1024)
        if cmd:
            cmd = cmd.split(" ")
            client.sendall(subprocess.check_output(cmd))
        else:
            client.close()
            break
