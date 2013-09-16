#! /usr/bin/env python

def get_digits(x):
    res = []
    while x > 0:
        res.append(int(x%10))
        x/=10
    res.reverse()
    return res

limit = 1000
s = 0
for x in xrange(1, limit+1):
    s += x**x
print s
last_digits = get_digits(s)[-10:]
print "".join(map(str, last_digits))

