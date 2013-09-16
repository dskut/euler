#! /usr/bin/env python

path = "13-large-sum.txt"
with open(path) as sum_file:
    #nums = [map(int, line.split()) for line in grid_file]
    s = sum([int(line) for line in sum_file])
    print s
    while s >= 1e10:
        s /= 10
    print s
