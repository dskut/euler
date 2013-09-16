#! /usr/bin/env python

s = list("0123456789")
limit = 1000000

def permute(s):
    k = -1
    for i in xrange(0, len(s) - 1):
        if s[i] < s[i+1]:
            k = i
    if k == -1:
        return None
    m = k+1
    for i in xrange(k+1, len(s)):
        if s[k] < s[i]:
            m = i
    s[k], s[m] = s[m], s[k]
    s[k+1:] = reversed(s[k+1:])
    return s

for i in xrange(2, limit+1):
    if not permute(s):
        break
print "".join(s)
