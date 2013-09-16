#! /usr/bin/env python

import math

def get_digits(x):
    res = []
    while x > 0:
        res.append(x%10)
        x/=10
    return res

limit = 9999999
s = 0
for x in xrange(3, limit):
    digits = get_digits(x)
    fac = sum([math.factorial(d) for d in digits])
    if fac == x:
        print x
        s += x
print "sum =", s

