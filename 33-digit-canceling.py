#! /usr/bin/env python

def eq(a,b):
    return abs(a-b) < 1e-7


fracs = []

for numer in xrange(11, 100):
    for denom in xrange(numer+1, 100):
        frac = float(numer)/denom
        numer_digits = [numer/10, numer%10]
        denom_digits= [denom/10, denom%10]

        if numer_digits[0] == denom_digits[0]:
            new_numer = numer_digits[1]
            new_denom = denom_digits[1]
            if new_denom == 0:
                continue
            new_frac = float(new_numer)/new_denom
            if eq(frac, new_frac):
                fracs.append((numer,denom))

        if numer_digits[1] == denom_digits[0]:
            new_numer = numer_digits[0]
            new_denom = denom_digits[1]
            if new_denom == 0:
                continue
            new_frac = float(new_numer)/new_denom
            if eq(frac, new_frac):
                fracs.append((numer,denom))

        if numer_digits[0] == denom_digits[1]:
            new_numer = numer_digits[1]
            new_denom = denom_digits[0]
            if new_denom == 0:
                continue
            new_frac = float(new_numer)/new_denom
            if eq(frac, new_frac):
                fracs.append((numer,denom))

        if numer_digits[1] == denom_digits[1]:
            if numer_digits[1] == 0:
                continue
            new_numer = numer_digits[0]
            new_denom = denom_digits[0]
            if new_denom == 0:
                continue
            new_frac = float(new_numer)/new_denom
            if eq(frac, new_frac):
                fracs.append((numer,denom))

print fracs

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    return a*b/gcd(a,b)

def reduce_frac(frac):
    d = gcd(frac[0], frac[1])
    return [frac[0]/d, frac[1]/d]

mult = 1
prod = [1,1]
for frac in fracs:
    mult = lcm(mult, frac[1])
    prod[0] *= frac[0]
    prod[1] *= frac[1]
    print mult
print mult
print prod
prod = reduce_frac(prod)
print prod

