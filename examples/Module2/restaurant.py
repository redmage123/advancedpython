#!/usr/bin/env python

# This example show the use of a custom comparator function. 

class Restaurant(object):

    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.rank = kwargs["rank"]


    def __str__(self):
        return "Restaurant %s has ranking %d" % (self.name,self.rank)


# Here is our custom comparator comparing the rank of the restaurant. 

    def __cmp__(self, other):
        if (self.rank < other.rank):
            return -1
        elif (self.rank == other.rank):
            return 0
        else:
            return 1




r1 = Restaurant(name="Alice's Restaurant",rank=3)
r2 = Restaurant(name = "Bob's Grill",rank=2)


# Compare by rank
if (r1 > r2): 
    print "Alice's is the best"
else:
    print "Bob's is the best"
