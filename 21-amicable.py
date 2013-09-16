#!/usr/bin/env python

import math

limit = 10000

def get_divisors(x):
    res = []
    sq = int(math.sqrt(x))
    for i in xrange(1, sq+1):
        if x % i == 0:
            res.append(i)
            if x/i != i and i != 1:
                res.append(x/i)
    return res

amicable = set()
for i in xrange(2, limit+1):
    divisors = get_divisors(i)
    other = sum(divisors)
    other_divisors = get_divisors(other)
    other_sum = sum(other_divisors)
    if other_sum == i and other != i:
        print i, other
        amicable.add(i)
        amicable.add(other)

print amicable
print sum(amicable)
