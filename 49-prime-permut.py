#! /usr/bin/env python

limit = 10000

def gen_primes():
    nums = [True]*limit
    primes = set() 
    for i in xrange(2, limit):
        if nums[i]:
            primes.add(i)
            for j in xrange(i*i, limit, i):
                nums[j] = False
    return primes

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

def get_permuts(x):
    digits = list(str(x))
    res = []
    digits = permute(digits)
    while digits:
        p = int("".join(digits))
        res.append(p)
        digits = permute(digits)
    return res

primes = gen_primes()
for prime in primes:
    permuts = get_permuts(prime)
    prime_permuts = []

    for permut in permuts:
        if permut in primes:
            prime_permuts.append(permut)

    if len(prime_permuts) < 3:
        continue

    prime_permuts.sort()
    #if prime_permuts[2] - prime_permuts[1] != prime_permuts[1] - prime_permuts[0]:
    #    continue

    print prime_permuts
