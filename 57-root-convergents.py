#! /usr/bin/env python

def digits(x):
    return len(str(x))

limit = 1000
x = 1
y = 1
count = 0
for i in xrange(0,limit+1):
    if digits(x) > digits(y):
        print x, "/", y
        count += 1
    dx = x + 2*y
    dy = x+y
    x = dx
    y = dy
print count
