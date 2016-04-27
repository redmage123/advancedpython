#!/usr/bin/python3
class addFunc(object):
    def __init__(self,base):
        self.base = base

    def __call__(self,extra):
        return self.base + extra


a = addFunc(2)
print (a(4))
