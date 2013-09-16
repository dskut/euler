#! /usr/bin/env python

limit = 1000000
triangs = set()
pents = set()
hexs = set()
for n in xrange(1, limit+1):
    t = n * (n+1) / 2
    triangs.add(t)
    p = n * (3*n - 1) / 2
    pents.add(p)
    h = n * (2*n - 1)
    hexs.add(h)

inter = triangs & pents & hexs
print inter
