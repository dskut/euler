#! /usr/bin/env python

max_s = 0
for a in xrange(1,100):
    for b in xrange(1,100):
        x = a**b
        digits = list(str(x))
        s = sum([int(d) for d in digits])
        if s > max_s:
            max_s = s
print max_s
