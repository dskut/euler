#! /usr/bin/env python

sort_nums = list('123456789')
def is_pandigit(s):
    return len(s) == 9 and sorted(s) == sort_nums 

m = 99999
for x in xrange(2, m/2):
    concat = ""
    for i in xrange(1, 10):
        mult = x*i
        concat += str(mult)
        if len(concat) > 9:
            break
        if is_pandigit(concat):
            print x, i, concat
