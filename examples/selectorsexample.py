#!/usr/bin/python3.5


import socket
import selectors


def accept(s,mask):

    conn,addr = s.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)
    conn.send("Registered client connection!\n".encode('UTF-8'))


def read(conn,mask):
    data = conn.recv(1024)

    if data:
        print ('Echoing',repr(data.decode('UTF-8')),'to', conn)
        conn.send(data)
    else:
        print ('Closing connection')
        sel.unregister(conn)
        conn.close()
       


# Here we're using the default selector rather than specifically
# selecting poll, epoll, or select.  Python will choose the most 
# optimal implementation for us.  
sel=selectors.DefaultSelector()


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)


server.bind(("localhost",10080))
server.listen(5)

# Register this descriptor with the selector.  We tell it that it's
# to notify us on any sort of read event and call the accept function
# when when a read event happens on this descriptor.

sel.register(server,selectors.EVENT_READ,accept)


while True:
# Note that the select method is is an abstract method, it isn't necessarily 
# related to the actual select() system call.  It's just the method used for 
# all implementations of the BaseSelector abstract class

# Events here is a reference to a SelectorKey class. This is a named
# tuple which consists of the following fields...
# The file object, i.e. in this case the registered socket.
# The file descriptor for this file object
# The events that we selected to wait on (The above code shows that 
# We're waiting on READ events. 
# A data field which, in this case, contains the callback function reference.

    events = sel.select()
    for key, mask in events:

    # Callback is now a reference to our callback function (i.e. the accept()
    # function in this case
        callback = key.data
        callback(key.fileobj,mask)


