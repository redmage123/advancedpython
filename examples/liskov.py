#!/usr/bin/python3
class Rectangle(object):
    def __init__(self,h,w):
        self.h = h
        self.w = w

    def setWidth(self,w):
        self.w = w

    def setHeight(self,h):
        self.h = h

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h
    
    def getArea(self):
        return self.w * self.h


class Square(Rectangle):

    def __init__(self,w,h):
        self.w = w
        self.h = h

    def setWidth(self,w):
        self.w = w
        self.h = w

    def setHeight(self,w):
        self.w = w
        self.h = w


r = Square(2,2)

r.setWidth(5)
r.setHeight(10)

print (r.getArea()) # Should be 50, but it's really 1990. 


