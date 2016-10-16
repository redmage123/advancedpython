#!/usr/bin/python3
from functools import total_ordering
@total_ordering
class Foo(object):

    def __init__(self,a):
        self.a = a

    def __lt__(self,other):
        return (True if self.a < other.a  else False)

    def __eq__(self,other):
        return (True if self.a == other.a else False)

    def __str__(self):
        return str(self.a)

f = Foo("Hello")
g = Foo("Goodbye")
h = Foo("World")
i = Foo("Planet")
j = Foo("Stuff")

fooList = []



if f < g:
    print ("f is less than g")
elif f == g:
    print ("F is equal to g")
else:
    print ("f is greater than g")

fooList.extend([f,g,h,i,j])

for foo in sorted(fooList):
    print (foo)
