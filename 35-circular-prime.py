#! /usr/bin/env python

limit = 1000000


nums = [True] * limit
def gen_primes():
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            for n in xrange(i*i, limit, i):
                nums[n] = False

gen_primes()

def count_digits(x):
    res = 0
    while x > 0:
        res += 1
        x /= 10
    return res

def rotate(x):
    digits_num = count_digits(x)
    res = []
    for i in xrange(0, digits_num):
        last_dig = x % 10
        x = last_dig * (10**(digits_num-1)) + x / 10
        res.append(x)
    return res



count = 0
for (i, is_prime) in enumerate(nums):
    if is_prime:
        rotations = rotate(i)
        if all([nums[x] for x in rotations]):
            print i
            count += 1
print "count =", count
