#!/bin/python3

import sys


def marsExploration(s):
    # Complete this function
    if len(s) % 3 != 0:
        return None
    n_msg = len(s) / 3
    cntr = 0
    for i in range(0, len(s), 3):
        tmp = s[i:i + 3]
        if tmp[0] != 'S':
            cntr += 1
        if tmp[1] != 'O':
            cntr += 1
        if tmp[2] != 'S':
            cntr += 1
    return cntr

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
