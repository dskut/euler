#! /usr/bin/env python

import math

limit = 1000
solutions = [0]*limit
for a in xrange(1, limit/2):
    for b in xrange(a+1, limit/2):
        c2 = a*a + b*b 
        c = int(math.sqrt(c2))
        if abs(float(c2) / c - c) < 1e-6:
            perim = a + b + c
            if perim < limit:
                solutions[perim] += 1
                print a,b,c

print max((v, i) for i, v in enumerate(solutions))[1]
