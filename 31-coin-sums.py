#! /usr/bin/env python

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def get_coins_impl(x, min_coin):
    if x == 0:
        return [[]] 
    res = []
    for coin in coins:
        if coin < min_coin:
            continue
        if coin <= x:
            changes = get_coins_impl(x - coin, coin)
            for change in changes:
                change = [coin] + change
                res.append(change)
    return res


def get_coins(x):
    return get_coins_impl(x, coins[0])

#changes = get_coins(200)
#print len(changes)

def get_change_ways(amount):
    ways = [0]*(amount+1)
    ways[0] = 1
    for coin in coins:
        for i in xrange(coin, amount+1):
            ways[i] += ways[i - coin] 
    return ways[amount]

print get_change_ways(200)

