#!/usr/bin/python3

''' Simple class showing how to use the super() method in Python '''

class Parent(object):
    def __init__(self):
        print("In parent\n")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print ("In child\n")

c = Child()
