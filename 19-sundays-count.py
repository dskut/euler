#! /usr/bin/env python

import time
from datetime import date, timedelta

t = time.strptime("19010101", "%Y%m%d")
t = date(t.tm_year, t.tm_mon, t.tm_mday)
count = 0
while t.year <= 2000:
    if t.day == 1 and t.weekday() == 6:
        print t.strftime('%Y%m%d %A')
        count += 1
    t += timedelta(1)
print count
