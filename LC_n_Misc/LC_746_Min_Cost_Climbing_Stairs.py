class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        res = [0] * (n)
        res[0], res[1] = cost[0], cost[1]

        for i in range(2, n):
            res[i] = cost[i] + min(res[i-1], res[i-2])

        return min(res[n-1], res[n-2])

obj = Solution()
print(obj.minCostClimbingStairs([10,15,20]))
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
