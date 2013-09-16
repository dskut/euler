#! /usr/bin/env python

import math

limit = 200000000
#primes = [True] * limit
def gen_primes():
    primes[0] = primes[1] = False
    for (i, is_prime) in enumerate(primes):
        if is_prime:
            for n in xrange(i*i, limit, i):
                primes[n] = False
#gen_primes()

def is_prime(x):
    if x == 1:
        return False
    sq = int(math.sqrt(x))
    if sq*sq == x:
        return False
    count = 0
    for i in xrange(1, sq+1):
        if x % i == 0:
            count += 1
    return count == 1

bottom_left = 1
side = 1
prime_count = 0
while True:
    top_right = bottom_left + 2*side
    side += 2
    if is_prime(top_right):
        prime_count += 1

    top_left = top_right + side - 1
    if is_prime(top_left):
        prime_count += 1

    bottom_left = top_left + side - 1
    if is_prime(bottom_left):
        prime_count += 1

    total_diag = side*2 - 1
    frac = float(prime_count)/total_diag
    print side, frac
    if frac < 0.1:
        break


