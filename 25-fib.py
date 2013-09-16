#! /usr/bin/env python
fib = []
prev = 1
fib = 1
count = 2
while fib < 10**999:
    tmp = fib + prev
    prev = fib
    fib = tmp
    count += 1
print count
