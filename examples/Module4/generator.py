#!/usr/bin/python3
import math

def mygen(n):
    print ("in mygen")
    num=0
    while num < n:
        print ("num = " + str(num))
        yield num
        num +=1



print(sum(mygen(4)))



