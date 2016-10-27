#!/usr/bin/python3

from collections import defaultdict

d = {}

# Here we use the setdefault method from the python dictionary to 
# set the default value for the key 'foo' in dictionary d to 0. 
# However, the problem here is that we need to do this for every key
# that we expect to be able to insert if we don't want to get a
# KeyErrorException thrown when accessing d['foo'] if it hasn't
# already got a value.

d.setdefault('foo',0)
print (d['foo'])


# Better way.  Make d a defaultdict.  Note that we have to pass into
# the constructor a callable object.  You can look in the Python
# documentation for built in functions to find the callable built in
# objects (or create and pass in your own callable object). Passing
# an int object automatically means that the defaultdict will set a value 
# of 0 for any undefined key/value pairs. 

d = defaultdict(int)

# Now, everytime we try to print out a key that doesn't exist in the
# dictionary, we get a 0 printed instead of an exception thrown.

print (d['foo'])
