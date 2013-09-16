#! /usr/bin/env python

limit = 1001

s = 1
x = 1
counter = 0
inc = 0
print x
while True:
    if counter % 4 == 0:
        if inc == limit - 1:
            break
        inc += 2
    counter += 1
    x += inc
    print x
    s += x
print "s = ", s


