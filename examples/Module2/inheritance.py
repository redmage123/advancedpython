#!/usr/bin/python3


''' Simple class showing how inheritance works in Python '''

class Parent(object):
    def __init__(self):
        pass
    def Method1(self):
        print("In parent\n")

class Child(Parent):
    def __init__(self):
        pass
    def Method1(self):
        print ("In child\n")

c = Child()
c.Method1()
