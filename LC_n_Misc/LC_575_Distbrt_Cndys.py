class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies)//2, len(set(candies)))


obj = Solution()
print(obj.distributeCandies([1,1,2,2,3,3]))
print(obj.distributeCandies([1,1,2,3]))