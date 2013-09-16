#! /usr/bin/env python

max_num = 2000000

def primes(limit):
    nums = [True] * limit
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in xrange(i*i, limit, i):
                nums[n] = False

s = 0
for p in primes(max_num):
    s += p
print s
