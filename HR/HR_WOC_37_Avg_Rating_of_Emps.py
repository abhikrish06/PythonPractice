#!/bin/python3

import os
import sys
import decimal

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    res = []
    for val in rating:
        if val >= 90:
            res.append(val)

    #fin_rat = sum(res)/len(res)
    return decimal.Decimal(sum(res)/len(res)).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    print(averageOfTopEmployees(rating))
