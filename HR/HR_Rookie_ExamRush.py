#!/bin/python3

import sys

def examRush(tm, t):
    # Complete this function
    srt_tm = sorted(tm)
    #print(srt_tm)
    val = 0
    for i in srt_tm:
        bal = t - i
        if bal < 0:
            return val
        else:
            val += 1
            t -= i
    return val

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    tm = []
    tm_i = 0
    for tm_i in range(n):
        tm_t = int(input().strip())
        tm.append(tm_t)
    result = examRush(tm, t)
    print(result)
