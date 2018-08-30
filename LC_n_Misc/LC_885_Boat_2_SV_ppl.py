import math


class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people:
            return 0

        people = sorted(people, reverse=True)
        n = len(people)
        lo, hi = 0, n - 1
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                hi -= 1
            lo += 1

        return lo


obj = Solution()
print(obj.numRescueBoats([1, 2], 3))
print(obj.numRescueBoats([3, 5, 3, 4], 5))
print(obj.numRescueBoats([3, 8, 7, 1, 4], 9))
print(obj.numRescueBoats([3, 2, 2, 1], 3))
