#! /usr/bin/env python

import math

limit = 200000000
test_limit = 50000

def gen_primes(limit):
    nums = [True] * limit
    primes = set()
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            primes.add(i)
            for n in xrange(i*i, limit, i):
                nums[n] = False
    return primes

primes = gen_primes(limit)

def check_is_prime(n):
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n%divisor == 0:
            return False
    return True

def is_prime(x):
    if x < limit:
        return x in primes
    else:
        return check_is_prime(x)

def test_pair(a, b):
    ab = int(str(a) + str(b))
    if not is_prime(ab):
        return False
    ba = int(str(b) + str(a))
    if not is_prime(ba):
        return False
    return True

def test(first, second, third, fourth, fifth):
    x = [first, second, third, fourth, fifth]
    for a in x:
        for b in x:
            if a == b:
                continue
            if not test_pair(a,b):
                return False
    return True

primes_list = sorted(list(primes))
primes_list = [x for x in primes_list if x < test_limit]
useless_primes = set([2,5])

for first in primes_list:
    if first in useless_primes:
        continue
    #print first
    for second in primes_list:
        if second <= first or second in useless_primes:
            continue
        if not test_pair(first, second):
            continue
        #print first, second
        for third in primes_list:
            if third <= second or third in useless_primes:
                continue
            if not test_pair(first, third) or not test_pair(second, third):
                continue
            #print first, second, third
            for fourth in primes_list:
                if fourth <= third or fourth in useless_primes:
                    continue
                if not test_pair(first, fourth) or not test_pair(second, fourth) or not test_pair(third, fourth):
                    continue
                print first, second, third, fourth
                for fifth in primes_list:
                    if fifth <= fourth or fifth in useless_primes:
                        continue
                    if not test_pair(first, fifth) or not test_pair(second, fifth) or not test_pair(third, fifth) or not test_pair(fourth, fifth):
                        continue
                    print first, second, third, fourth, fifth, " = ", sum([first, second, third, fourth, fifth])

