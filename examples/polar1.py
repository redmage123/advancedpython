#!/usr/bin/env python
import math


cart=[(1,1),(1,3),(2,5),(3,4)]


def carttopolar(t):
    r = math.sqrt(t[0] **2 + t[1]**2)
    try:
        theta = math.atan(t[1]/t[0])
    except ZeroDivisionError:
        theta = math.pi/2
    return(r,theta)

polar = map(lambda t: (math.sqrt(math.pow(t[0],2)  + math.pow(t[1],2)),math.atan(t[1]/t[0])),cart)

print polar
