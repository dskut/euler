#! /usr/bin/env python

N=20

matrix = [[0] * (N+1)] * (N+1)

for i in xrange(0,N+1):
    matrix[i][0] = 1
    matrix[0][i] = 1

for i in xrange(1,N+1):
    for j in xrange(1, N+1):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

print matrix[N][N]
