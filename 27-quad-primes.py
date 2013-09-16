#! /usr/bin/env python

limit = 1000

def gen_primes(limit):
    nums = [True] * limit
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            for n in xrange(i*i, limit, i):
                nums[n] = False
    return nums

primes = gen_primes(limit*limit)

max_a = 0
max_b = 0
max_n = 0
for a in xrange(-limit+1, limit):
    for b in xrange(-limit+1, limit):
        n = 0
        while True:
            x = n*n + a*n + b
            if not primes[x]:
                break
            n += 1
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b

print max_a, max_b, max_n
print max_a*max_b

            

