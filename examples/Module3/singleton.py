#!/usr/bin/python3

# This is an example of the Singleton design pattern 

class OnlyOne:

    class __OnlyOne:

        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(__OnlyOne) + self.val

    instance = None

# Note here that we check if the static class variable instance is set,
# if not, then set it.

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

x = OnlyOne("foo")
print (x.__OnlyOne)
y = OnlyOne("bar")
print (y.__OnlyOne)
