#! /usr/bin/env python

def get_num(a1, a2, a3, a4, a5, a6):
    return a6 + 10*(a5 + 10*(a4 + 10*(a3 + 10*(a2 + 10*(a1))))) 

summ = 0
for a1 in xrange(0, 10):
    for a2 in xrange(0, 10):
        for a3 in xrange(0, 10):
            for a4 in xrange(0, 10):
                for a5 in xrange(0, 10):
                    for a6 in xrange(0, 10):
                        s = a1**5 + a2**5 + a3**5 + a4**5 + a5**5 + a6**5
                        n = get_num(a1, a2, a3, a4, a5, a6)
                        if s == n and n > 1:
                            print n
                            summ += n

print "sum =", summ
