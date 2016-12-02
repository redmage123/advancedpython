#!/usr/bin/python3

from collections import namedtuple
# Here we create a standard tuple of personnel information that contains
# the following fields, first name, last name, Employee ID and Address

standardtuple = ('Braun','Brelin','12345','1234 Main Street')

# With a standard tuple, if I want to access the first and last name, I need to 
# specify it with the index value of the tuple, i.e. first name is index 
# position 0, last name is index position 1.

print (standardtuple[0] + " "+ standardtuple[1])

# Let's see how to do the same thing with a named tuple.

# We use the named tuple factory to create a named tuple type called 'Person'
# The first argument is the named tuple's name, the second argument is the
# list of fields
Person = namedtuple('Person','firstname lastname ID Address')

# Now we can use this named tuple type to create Persons.  Such as:

Braun = Person('Braun','Brelin','12345','1234 Main Street')

# Note here that we can now access elements by field name, rather than
# index position
print (Braun.firstname + " " + Braun.lastname)

# We can create a person object by using the _make method and passing some
# sort of iterable data structure such as a list.

Bob=Person('Bob','Bird','12346','2345 Main Street')
print (Bob.firstname + " " + Bob.lastname)



