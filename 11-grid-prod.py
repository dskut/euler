#! /usr/bin/env python

path = "11-grid.txt"
with open(path) as grid_file:
    nums = [map(int, line.split()) for line in grid_file]
    
max_horiz = 0
best_i = 0
best_j = 0
for i in xrange(0, 20):
    line = nums[i]
    prod = line[0]*line[1]*line[2]*line[3]
    if prod > max_horiz:
        max_horiz = prod
        best_i = i
        best_j = 3
    for j in xrange(4,20):
        if (line[j-4] == 0):
            prod = line[j-3]*line[j-2]*line[j-1]*line[j]
        else:
            prod = prod / line[j-4] * line[j]
        if prod > max_horiz:
            max_horiz = prod
            best_i = i
            best_j = j


print max_horiz

max_vert = 0
best_i = 0
best_j = 0
for j in xrange(0, 20):
    prod = nums[0][j]*nums[1][j]*nums[2][j]*nums[3][j]
    if prod > max_vert:
        max_vert = prod
        best_i = 3
        best_j = j
    for i in xrange(4, 20):
        if nums[i-4][j] == 0:
            prod = nums[i-3][j]*nums[i-2][j]*nums[i-1][j]*nums[i][j]
        else:
            prod = prod / nums[i-4][j] * nums[i][j]
        if prod > max_vert:
            max_vert = prod
            best_i = i
            best_j = j

print max_vert

max_bottomleft = 0
best_i = best_j = 0
for i in xrange(0, 17):
    for j in xrange(0, 17-i):
        prod = nums[i+j][j]*nums[i+j+1][j+1]*nums[i+j+2][j+2]*nums[i+j+3][j+3]
        #print nums[i+j][j], nums[i+j+1][j+1], nums[i+j+2][j+2], nums[i+j+3][j+3]
        if prod > max_bottomleft:
            max_bottomleft = prod
        #    best_i = i 
        #    best_j = j

print max_bottomleft
#print best_i
#print best_j

max_topright = 0
for j in xrange(1, 17):
    for i in xrange(0, 17-j):
        prod = nums[i][i+j] * nums[i+1][i+j+1] * nums[i+2][i+j+2] * nums[i+3][i+j+3]
        #print nums[i][i+j], nums[i+1][i+j+1], nums[i+2][i+j+2], nums[i+3][i+j+3]
        if prod > max_topright:
            max_topright = prod

print max_topright

max_topleft = 0
for i in xrange(3, 20):
    for j in xrange(0, i-2):
        prod = nums[i-j][j] * nums[i-j-1][j+1] * nums[i-j-2][j+2] * nums[i-j-3][j+3]
        if prod > max_topleft:
            max_topleft = prod

print max_topleft

#for j in xrange(16, 1, -1):
    #print("j = %d" % j)
    #for i in xrange(16, j, -1):
        #print("i = %d" % i)
        #print nums[i][17+i-j], nums[i-1][i-j-1], nums[i-2][i-j-2], nums[i-3][i-j-3]

