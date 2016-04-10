#!/usr/bin/python

class foo(object):
    def __init__(blech):
        blech.bar = "bar"
        blech.baz = "baz"

    def printstuff(blech):

        print(blech.bar + "\n")
        print(blech.baz + "\n")


f = foo()
f.printstuff()

