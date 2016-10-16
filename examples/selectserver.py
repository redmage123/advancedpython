#!/usr/bin/python3


import socket
import select
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)
server.bind(("localhost",10080))
server.listen(5)

inputs = [server]
outputs = []

while inputs:
    readable,writable,exceptional = select.select(inputs,outputs,inputs)

    for s in readable:
        if s is server:
            print ("s is server")
            connection,client_address = s.accept()
            connection.setblocking(0)
            data = connection.recv(1024)
            sendString = "Got " + data.decode()
            connection.send(sendString.encode())
            inputs.append(connection)
        else:
            data = s.recv(1024)
            if data:
                sendString = "Got " + data.decode()
                s.send(sendString.encode())
            else:
                s.close()
