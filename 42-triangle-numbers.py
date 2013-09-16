#! /usr/bin/env python

import re

def get_code(word):
    res = 0
    for c in word:
        res += ord(c) - ord('a') + 1
    return res

def gen_triangle():
    res = set() 
    limit = 30*26/2
    for i in xrange(1, limit):
        x = i*(i+1)/2
        res.add(x)
    return res

with open("42-words.txt") as f:
    words = []
    for line in f:
        words += re.findall("\w+", line)
    words = map(lambda x: x.lower(), words)

triang_nums = gen_triangle()

count = 0
for word in words:
    code = get_code(word)
    if code in triang_nums:
        print word
        count += 1
print count
