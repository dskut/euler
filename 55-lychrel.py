#! /usr/bin/env python

limit = 10000
max_iter = 50

def is_lychrel(x):
    for i in xrange(0, max_iter):
        l = list(str(x))
        rev_s = "".join(reversed(l))
        rev = int(rev_s)
        if i != 0 and rev == x:
            return False
        x += rev
    return True

count = 0
for x in xrange(1, limit):
    if is_lychrel(x):
        print x
        count += 1
print "count =", count
