#! /usr/bin/env python

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

nums = list("123456789")
prods = set()
while nums:
    s = "".join(nums)
    for i in xrange(1, len(nums)-1):
        for j in xrange(i+1, len(nums)):
            a = int(s[:i])
            b = int(s[i:j])
            prod = int(s[j:])
            if a*b == prod:
                print a, b, prod
                prods.add(prod)
    nums = permute(nums)
print sum(prods)
