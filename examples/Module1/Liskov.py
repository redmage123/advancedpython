#!/usr/bin/python3

 ''' Class showing an example of the Liskov Substitution Principle '''

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


# While mathematically, a square is a special type of Rectangle, it doesn't really fit well
# into the inheritance model.  

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


# Trying to make a square use the rectangle methods gives errors. 
r = Square(2,2)

r.setWidth(5)
r.setHeight(10)

print (r.getArea()) # Should be 50, but it's really 1990. 


