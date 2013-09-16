#! /usr/bin/env python

limit = 999999

for i in xrange(0, limit):
    s = sorted(str(i))
    s2 = sorted(str(i*2))
    if s != s2:
        continue
    s3 = sorted(str(i*3))
    if s != s3:
        continue
    s4 = sorted(str(i*4))
    if s != s4:
        continue
    s5 = sorted(str(i*5))
    if s != s5:
        continue
    s6 = sorted(str(i*6))
    if s != s6:
        continue
    print i
