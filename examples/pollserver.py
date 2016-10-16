#!/usr/bin/python3

import socket
import select
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)
TIMEOUT=1000

server.bind(("localhost",10080))
server.listen(5)

READ_ONLY = select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR
READ_WRITE = READ_ONLY | select.POLLOUT

poller = select.poll()
poller.register(server,READ_ONLY)

fd_to_socket = {server.fileno(): server,}


while True:
    events = poller.poll(TIMEOUT)

    for fd,flag in events:
        s = fd_to_socket[fd]
        
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                connection,client_address = s.accept()
                connection.setblocking(0)
                fd_to_socket [ connection.fileno() ] = connection
                poller.register(connection,READ_ONLY)
            else:
                data = s.recv(1024).decode()
                if data:
                    sendString = "Got " + data
                    s.send(sendString.encode())
                else:
                    poller.unregister(s)
                    s.close()







