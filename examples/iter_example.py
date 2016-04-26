#!/usr/bin/python

elements = [1,2,3,4,5]
it = iter(elements)
while True:
    try:
        print it.next()
    except StopIteration:
        break
