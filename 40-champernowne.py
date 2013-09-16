#!/usr/bin/env python

s = ""
inds = [1, 10, 100, 1000, 10000, 100000, 1000000]
for x in xrange(0, inds[-1]):
    s += str(x)

m = 1
for ind in inds:
    m *= int(s[ind])
print m
