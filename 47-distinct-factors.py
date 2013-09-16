#! /usr/bin/env python
from collections import defaultdict
from math import sqrt

def factor(n):
    res = set()
    i = 2
    limit = sqrt(n)    
    while i <= limit:
      if n % i == 0:
        res.add(i)
        n = n / i
        limit = sqrt(n)   
      else:
        i += 1
    if n > 1:
        res.add(n)
    return res

limit = 1000000000
fn = 4

first = factor(2)
second = factor(3)
third = factor(4)

for i in xrange(5, limit):
    fourth = factor(i)
    if len(first) == fn and len(second) == fn and len(third) == fn and len(fourth) == fn:
        print "==========================="
        print i - 3, first
        print i - 2, second
        print i - 1, third
        print i, fourth
    first = second
    second = third
    third = fourth


