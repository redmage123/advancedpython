#!/usr/bin/python3


# Classic example of something counterintuitively breaking the Liskov 
# Substitution Principle.  

class Rectangle(object):
    def __init__(self):

        self.width = 0
        self.height =0

    def setHeight(self,h):
        self.height =h

    def setWidth(self,w):
        self.width=w

    def getWidth(self):
        return self.width 

    def getHeight(self):
        return self.height 

    def getArea(self):
        return self.height * self.width 

class Square(Rectangle):

    def setWidth(self,w):
        self.width = w
        self.height = w

    def setHeight(self,h):
        self.width = h
        self.height = h


class RecFactory(object):
    def __init__(self):
        pass

    def getNewRectangle(self):
        return Square()


rf = RecFactory()
s = rf.getNewRectangle()
s.setWidth(5)
s.setHeight(10)

print(s.getArea())

