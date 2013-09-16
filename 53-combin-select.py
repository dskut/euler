#! /usr/bin/env python

import math

count = 0
for n in xrange(1, 101):
    for r in xrange(0, n+1):
        c = math.factorial(n) / math.factorial(r) / math.factorial(n-r)
        if c > 1000000:
            count += 1
print count
