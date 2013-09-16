#! /usr/bin/env python

def get_value(s):
    res = 0
    for c in s:
        res += ord(c) - 96
    return res

names = []
with open("22-names.txt") as f:
    for line in f:
        line_names = line.split(',')
        for name in line_names:
            name = name.replace('"', '').lower()
            names.append(name)

names.sort()
res = 0
for i in xrange(0, len(names)):
    pos = i + 1
    val = get_value(names[i])
    score = pos * val
    res += score
print res

