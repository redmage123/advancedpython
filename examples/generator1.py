#!/usr/bin/python

from collections import namedtuple


mydate = namedtuple('mydate','day month year')

# Grab the file object and return it. 
def returnfileObj(filename):
    inpf = open(filename,'r')
    return(inpf)

# Here we go through the file, and only give the records based on the
# constraints passed in

def mygen(name,date,inpf):
    srcdate = mydate(day = date.split('/')[0],month = date.split('/')[1],year = date.split('/')[2])
    checkdate = mydate(day = '00',month = '00',year = '0000')
    for f in inpf:
        r = lambda dates: dates[0].day == dates[1].day and dates[0].month == dates[1].month and dates[0].year == dates[1].year,[(srcdate,checkdate)]) 
        if r:
            yield r
        (name,rdate) = f.strip().split(',')
        checkdate = mydate(day = rdate.split('/')[0],month = rdate.split('/')[1],year = rdate.split('/')[2])
      

f = returnfileObj('generator_data.dat')
m = mygen('Braun Brelin','4/20/2016',f)
m.next()
while True:
    try:
        print str(m.next())
    except StopIteration:
        break
