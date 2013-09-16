#! /usr/bin/env python

cache = {1: 1}
def get_chain(n):
    if n in cache:
        return cache[n]
    x = n/2 if n % 2 == 0 else 3*n + 1
    chain = get_chain(x) + 1
    cache[n] = chain
    return chain

limit = 1000000
max_chain = 0
res = 1
for i in xrange(1, limit):
    chain = get_chain(i)
    if chain > max_chain:
        res = i
        max_chain = chain

print res
print max_chain
