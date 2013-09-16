#! /usr/bin/env python

def is_palindrome(l):
    return l == l[::-1]

def get_digits(x):
    res = []
    while x > 0:
        res.append(x%10)
        x/=10
    return res

def get_binary_digits(x):
    res = []
    while x:
        res.append(x&1)
        x = x >> 1
    return res 

limit = 1000000
s = 0
for x in xrange(1, limit):
    if is_palindrome(get_digits(x)) and is_palindrome(get_binary_digits(x)):
        print x
        s += x
print "sum =", s

