#! /usr/bin/env python

def num2str(x):
    if x == 1000:
        return"onethousand"
    res = ""
    if x >= 100:
        first_digit = x / 100
        res += num2str(first_digit) + "hundred"
        x %= 100
        if x == 0:
            return res
        res += "and"
    if x < 20 and x >= 10:
        res += {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}[x]
    elif x > 10:
        first_digit = x / 10
        res += {2:"twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy",
                8: "eighty", 9: "ninety"}[first_digit]
        last_digit = x % 10
        res += num2str(last_digit)
    elif x > 0:
        res += {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                6: "six", 7: "seven", 8: "eight", 9: "nine"}[x]
    return res

limit = 1000 
count = 0
for x in xrange(1, limit+1):
    s = num2str(x)
    print s
    count += len(s)
print count
