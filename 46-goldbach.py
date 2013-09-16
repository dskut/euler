#! /usr/bin/env python

import math

limit = 10000000
nums = [True] * limit
primes_list = []
def gen_primes():
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            primes_list.append(i)
            for n in xrange(i*i, limit, i):
                nums[n] = False

gen_primes()

def is_square(n):
    s = math.sqrt(n)
    i = int(s)
    return i*i == n

def check(x):
    for i in primes_list:
        if i >= x:
            return False
        rem = x - i
        if rem % 2 == 0 and is_square(rem/2):
            return True

for (i, is_prime) in enumerate(nums):
    if not is_prime and i % 2 != 0:
        if not check(i):
            print i


