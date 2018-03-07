#!/bin/python3

import os
import sys


# Complete the function below.

def maximumPackages(S, K, R, C):
    # Return the maximum number of packages that can be put in the containers.
    n = len(S)
    m = len(R)
    cntr = 0
    pckg_dict, cyl_dict = {}, {}

    for i in range(n):
        pckg_dict[S[i]] = K[i]

    for i in range(m):
        cyl_dict[R[i]] = C[i]

    for radius in sorted(cyl_dict.keys(), reverse=True):
        for edge in sorted(pckg_dict.keys(), reverse=True):
            if (2 ** 0.5) * (edge) < 2 * (radius):
                if cyl_dict[radius] > 0:
                    if cyl_dict[radius] == pckg_dict[edge]:
                        cntr = cntr + cyl_dict[radius]
                        cyl_dict[radius] -= cntr
                        pckg_dict[edge] -= cntr
                    elif cyl_dict[radius] > pckg_dict[edge]:
                        cntr = cntr + pckg_dict[edge]
                        cyl_dict[radius] -= cntr
                        pckg_dict[edge] -= cntr
                    elif cyl_dict[radius] < pckg_dict[edge]:
                        cntr = cntr + cyl_dict[radius]
                        cyl_dict[radius] -= cntr
                        pckg_dict[edge] -= cntr

    return cntr


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    # S_size = int(input())

    S = list(map(int, input().rstrip().split()))

    # K_size = int(input())

    K = list(map(int, input().rstrip().split()))

    # R_size = int(input())

    R = list(map(int, input().rstrip().split()))

    # C_size = int(input())

    C = list(map(int, input().rstrip().split()))

    result = maximumPackages(S, K, R, C)

    f.write(str(result) + "\n")

    f.close()
