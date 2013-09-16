#! /usr/bin/env python

def check_cycle(divs, r):
    for i in xrange(0, len(divs)):
        if divs[i] == r:
            return len(divs) - i


limit = 1000
def get_recurring_cycle(x):
    r = 1
    divs = [] 
    while True:
        while r < x:
            r *= 10
        cycle = check_cycle(divs, r)
        if cycle:
            return cycle
        divs.append(r)
        d = r / x
        r = (r - d*x)
        if r == 0:
            return None


max_cycle = 0
max_i = 0
for i in xrange(2, limit+1):
    cycle = get_recurring_cycle(i)
    if cycle:
        print "cycle:", i, cycle
        if cycle > max_cycle:
            max_cycle = cycle
            max_i = i
print "res", max_i, max_cycle
