#! /usr/bin/env python

limit = 999999
family_size = 8

def gen_primes():
    nums = [True] * limit
    nums[0] = nums[1] = False
    prime_set = set() 
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            prime_set.add(i)
            for n in xrange(i*i, limit, i):
                nums[n] = False
    return prime_set 

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

def get_permuts(s):
    res = []
    res.append("".join(s))
    while permute(s):
        res.append("".join(s))
    return res

def gen_permuts(n):
    res = []
    for i in xrange(1, n):
        s = ['0']*i + ['1']*(n-i)
        res += get_permuts(s)
    return res

def gen_permuts_array():
    res = []
    res.append([])
    for i in xrange(0, len(str(limit))):
        p = gen_permuts(i+1)
        res.append(p)
    return res

def apply_mask(s, mask, digit):
    n = len(s)
    res = list(s)
    for i in xrange(0, n):
        if mask[i] == '1':
            res[i] = str(digit)
    return "".join(res)

def gen_masked(x, mask):
    s = str(x)
    res = []
    start = 1 if mask[0] == '1' else 0
    for digit in xrange(start, 10):
        r = apply_mask(s, mask, digit)
        res.append(int(r))
    return res

primes = gen_primes()
permuts_array = gen_permuts_array()

seen = set()
min_res = limit
for prime in primes:
    if prime in seen:
        continue
    prime_len = len(str(prime))
    permut_bits = permuts_array[prime_len]
     
    for mask in permut_bits:
        masked = gen_masked(prime, mask)
        filtered = filter(lambda m: m in primes, masked)
        seen |= set(filtered)

        if len(filtered) == family_size:
            print prime, filtered
            min_res = min(filtered + [min_res])

print "res =", min_res
