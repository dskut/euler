#! /usr/bin/env python

limit = 10000000
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

def trunc_left(x):
    res = []
    count = count_digits(x)
    while count > 0:
        res.append(x)
        x = x % (10**(count-1))
        count -= 1
    return res

def trunc_right(x):
    res = []
    while x > 0:
        res.append(x)
        x /= 10
    return res

limit = 11
count = 0
s = 0
for (i, is_prime) in enumerate(nums):
    if (is_prime and not i in [2,3,5,7] 
        and all(map(lambda x: nums[x], trunc_left(i))) 
        and all(map(lambda x: nums[x], trunc_right(i)))):
        print i
        s += i
        count += 1
        if count == limit:
            break

print "sum =", s

