#!/bin/python3

import sys

n = int(input().strip())

print(max(bin(n).strip('0b').split('0')).count('1'))
# print(max(bin(n).strip('0b').split('0')).count('1'))

print(len(max(bin(n).strip('0b').split('0'))))
