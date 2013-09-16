#! /usr/bin/env python

import math

def test_prime(x):
    sq = int(math.sqrt(x)+1)
    for i in xrange(2, sq+1):
        if x % i == 0:
            return False
    return True

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

for nums in ['1234', '12345', '123456', '1234567', '12345678', '123456789']:
    nums = list(nums)
    while nums:
        x = int("".join(nums))
        if test_prime(x):
            print x
        nums = permute(nums)
