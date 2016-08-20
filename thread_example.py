#!/usr/bin/python3

import threading


def foo(params):
    print (str(params))

def bar(params):
    print (str(params))

def baz(params):
    print (params)


class myThread(threading.Thread):
    def __init__(self,func,param):
        threading.Thread.__init__(self)
        self.func = func
        self.param =param

    def run(self):
        print ("func = " + str(self.func))
        print ("param = " + str(self.param))
        self.func(self.param)

t1 = myThread(foo,{"blech":"foo"})
t2 = myThread(bar, {"blech": "bar"})
t3 = myThread(baz,{"blech": "baz"})

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print ("Exiting main thread")
