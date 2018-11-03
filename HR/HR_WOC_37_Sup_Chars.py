#!/bin/python3

import os
import sys

# Complete the maximumSuperiorCharacters function below.
def maximumSuperiorCharacters(freq):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    big_lst = []
    for i, val in enumerate(alp):
        if freq[i] > 0:
            big_lst.append(val*freq[i])
    print(''.join(big_lst))
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        freq = list(map(int, input().rstrip().split()))

        result = maximumSuperiorCharacters(freq)

        # fptr.write(str(result) + '\n')

    # fptr.close()
