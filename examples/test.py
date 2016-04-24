#!/usr/bin/python3
import os
import shlex

with open ('./test.dat','r') as t:
    for r in t:
#        print (r.strip().split(' '))
        (a,b,c) = shlex.split(r)

        print (a[1:-1])
        print (b[1:-1])
        print (c[1:-1])

