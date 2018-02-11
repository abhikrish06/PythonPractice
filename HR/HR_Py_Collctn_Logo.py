#!/bin/python3

import sys

if __name__ == "__main__":
    s = input().strip()

d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d=sorted(d.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    print(' '.join(map(str,d[i])))

# Another soln using OrderedCounter
# !/bin/python3

import sys
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict): # for more on OrderedCounter visit: https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/
    pass


if __name__ == "__main__":
    s = input().strip()

for c in OrderedCounter(sorted(s)).most_common(3):
    print(' '.join(map(str, c)))
