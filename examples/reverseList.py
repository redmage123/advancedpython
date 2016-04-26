#!/usr/bin/python

class reverseList():

    def __init__(self):
        self.data = []
        self.len=0
        self.count=0

    def next(self):
        if self.count < 0:
            raise StopIteration

        rval = self.data[self.count]
        self.count -= 1
        return (rval)

    def __iter__(self):
        self.count = self.len -1
        return self

    def append(self,obj):
        self.data.append(obj)
        self.len +=1

r = reverseList()
r.append(1)
r.append(2)

for e in r:
    print e
