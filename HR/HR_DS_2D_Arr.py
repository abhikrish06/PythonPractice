#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

# print(arr[])
arr_temp = []
for i in range(len(arr) - 2):
    for j in range(len(arr) - 2):
        # print(arr[i][j], arr[i][j + 1] , arr[i][j + 2])
        # print(arr[i + 1][j + 1])
        # print(arr[i + 2][j] , arr[i + 2][j] , arr[i+2][j + 2])
        # print('\n')
        arr_temp.append(sum(arr[i][j:j+3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j+3]))
        #arr_temp.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j+1] + arr[i+2][j + 2])

#print(arr_temp)
print(max(arr_temp))
# print(arr)
