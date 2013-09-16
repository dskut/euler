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

def check_substr(nums):
    if int("".join(nums[1:4])) % 2 != 0:
        return False
    if int("".join(nums[2:5])) % 3 != 0:
        return False
    if int("".join(nums[3:6])) % 5 != 0:
        return False
    if int("".join(nums[4:7])) % 7 != 0:
        return False
    if int("".join(nums[5:8])) % 11 != 0:
        return False
    if int("".join(nums[6:9])) % 13 != 0:
        return False
    if int("".join(nums[7:10])) % 17 != 0:
        return False
    return True

nums = list("0123456789")
s = 0
while nums:
    if check_substr(nums):
        x = int("".join(nums))
        print x
        s += x
    nums = permute(nums)
print "sum =", s
