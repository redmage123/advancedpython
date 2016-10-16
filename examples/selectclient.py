import socket
import sys


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect("localhost",10080)

if client:
    client.send("Foo")
    client.recv(1024)
    client.close

