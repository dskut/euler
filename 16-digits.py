#!/usr/bin/env python

p = 1000
b = 2

res = b**p
print res

s = 0
while res > 0:
    s += res % 10
    res /= 10
print s
