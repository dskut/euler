#! /usr/bin/env python

limit = 1000000
def gen_primes():
    nums = [True] * limit
    nums[0] = nums[1] = False
    primes = []
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            primes.append(i)
            for n in xrange(i*i, limit, i):
                nums[n] = False
    return primes 

primes = gen_primes()
primes_set = frozenset(primes)

max_consec = []
for i in xrange(0, len(primes)):
    s = primes[i]
    consec = [primes[i]] 
    for j in xrange(i+1, len(primes)):
        s += primes[j]
        consec.append(primes[j])
        if s in primes_set and len(consec) > len(max_consec):
            max_consec = consec[:]
    print sum(max_consec), max_consec


