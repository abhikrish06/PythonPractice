# if n % 2 == 0:
#     print("median:", (scr_lst[(n // 2) - 1] + scr_lst[(n // 2)]) / 2)
# else:
#     p = math.floor(n / 2)
#     print("median:", scr_lst[p])

import numpy as np
import pandas as pd
import math


def cal_med(num):
    print(num)
    n = len(num)
    if n % 2 == 0:
        return (int(num[(n // 2) - 1]) + int(num[(n // 2)])) / 2
    else:
        p = math.floor(n / 2)
        return int(num[p])

if __name__ == '__main__':
    numbers = []
    n = int(input())
    numbers = map(int, input().split())
    nums = sorted(numbers)
    print("numbers: ", nums)
    #print(mid)
    print("Q1: ", cal_med(nums[:len(nums)//2]))
    print("Q2: ", cal_med(nums))
    if n % 2 == 0:
        print("Q3: ", cal_med(nums[len(nums)//2:]))
    else:
        print("Q3: ", cal_med(nums[len(nums) // 2 + 1:]))

# 12 54 89 65 9
# 12 34 10 9 23 34
