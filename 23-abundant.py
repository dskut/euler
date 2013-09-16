#! /usr/bin/env python
import math

def get_divisors(x):
    res = []
    sq = int(math.sqrt(x))
    for i in xrange(1, sq+1):
        if x % i == 0:
            res.append(i)
            if x/i != i and i != 1:
                res.append(x/i)
    return res

def is_abundant(x):
    return x < sum(get_divisors(x))

limit = 28123
abundants = []
for i in xrange(1, limit+1):
    if is_abundant(i):
        abundants.append(i)

res = set(range(1, limit+1))
for i in xrange(0, len(abundants)):
    for j in xrange(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s <= limit and s in res:
            res.remove(s)

print sum(res)

