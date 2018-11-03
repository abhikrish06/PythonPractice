#!/bin/python3

import os
import sys


# Complete the findTheAbsentStudents function below.
class Solution():
    def findTheAbsentStudents(self,n, a):
        set_a = set(a)
        res = []
        for i in range(1,n+1):
            if i in set_a:
                continue
            else:
                res.append(i)
        return sorted(res)


# Return the list of student IDs of the missing students in increasing order.

obj = Solution()
print(obj.findTheAbsentStudents(10, [1,2,2,3,4,5,2,8,9,10]))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     a = list(map(int, input().rstrip().split()))
#
#     result = findTheAbsentStudents(n, a)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
