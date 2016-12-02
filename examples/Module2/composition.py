#!/usr/bin/python3

from abc import ABCMeta, abstractmethod

''' Example illustrating the concept of abstract base classes in Python '''

# This is the abstract base class

class Transmission(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def transmission1(self):
        return


class Car(object):
    def __init__(self):
        pass

class Toyota(Car):
    def __init__(self):
        pass
    def transmission1(self):
        return "transmission1"


Transmission.register(Car)
    
t = Toyota()
print(t.transmission1() + "\n")


