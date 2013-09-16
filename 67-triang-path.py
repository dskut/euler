#! /usr/bin/env python

path = "67-triang.txt"
triang = []
with open(path) as tf:
    for line in tf:
        nums = map(int, line.split())
        triang.append(nums)

for i in xrange(len(triang)-2, -1, -1):
    nums = triang[i]
    for j in xrange(0, len(nums)):
        nums[j] += max(triang[i+1][j], triang[i+1][j+1])

print triang[0][0]

