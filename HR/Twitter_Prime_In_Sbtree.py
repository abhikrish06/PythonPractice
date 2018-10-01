#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the primeQuery function below.

def sieveOfEratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si * si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]


def allPrimes(values):
    primes = sieveOfEratosthenes(10 ** 5)
    pri = []
    for val in values:
        if val in primes:
            pri.append(val)
    return pri


def primeQuery(n, first, second, values, queries):
    prime_values = allPrimes(values)
    print(prime_values)
    res = [len(prime_values)]
    # tree construction
    for x, y in sorted(zip(first, second)):
        print(x,y)
    return

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'wb')

    n = int(input().strip())

    first_count = int(input().strip())

    first = []

    for _ in range(first_count):
        first_item = int(input().strip())
        first.append(first_item)

    second_count = int(input().strip())

    second = []

    for _ in range(second_count):
        second_item = int(input().strip())
        second.append(second_item)

    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    res = primeQuery(n, first, second, values, queries)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()
