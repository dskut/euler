#! /usr/bin/env python

limit = 10000
pent_set = set()
pent_arr = []
for i in xrange(1, limit+1):
    x = i * (3*i - 1) / 2
    pent_set.add(x)
    pent_arr.append(x)

min_d = pent_arr[-1]
for i in xrange(0, limit):
    pent_i = pent_arr[i]
    for j in xrange(i+1, limit):
        pent_j = pent_arr[j]
        s = pent_i + pent_j
        d = pent_j - pent_i
        if s in pent_set and d in pent_set:
            print pent_i, pent_j, d
            if d < min_d:
                min_d = d

print "min =", min_d

