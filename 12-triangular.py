#! /usr/bin/env python

import math

def factors_count(n):
    if n == 1:
        return [1]
    sq = int(math.sqrt(n))
    #count = 0
    res = []
    for i in xrange(1, sq+1):
        if n % i == 0:
            res.append(i)
            if n/i != i:
                res.append(n/i)
            #count += 2
    #if n == sq*sq:
        #count += 1
        #res.append(sq)
    #return count
    res.sort()
    return res

triang = 0
add = 0
limit = 501
while True:
    add += 1
    triang += add
    factors = factors_count(triang)
    print "%d : %s" % (triang, ", ".join(map(str, factors)))
    if len(factors) > limit:
        break

print triang
