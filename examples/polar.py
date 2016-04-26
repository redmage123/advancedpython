#!/usr/bin/env python


cart=[(1,1),(1,3),(2,5)]


def carttopolar(t):
    r = math.sqrt(t[0] **2 + t[1]**2)
    try:
        theta = math.atan(t[1]/t[0])
    except ZeroDivisionError:
        theta = math.pi/2
    return(r,theta)

polar = map(carttopolar,cart)

