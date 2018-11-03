# n = 0, ways = 1
# n = 1, ways = 1
# n = 2, ways = 2 [(1,1), (2)]
# n = 3, ways = 3 [(1,2), (2,1), (1,1,1)]
# n = 4, ways = 5  [(1,1,1,1), (2,2), (1,1,2), (1,2,1), (2,1,1)]
# https://www.youtube.com/watch?v=5o-kdjv7FD0

class Solution:

    dct = {}

    def climbStairs(self, n):
        if n == 0 or n == 1:
            val = 1

        if n >= 2:
            if n in self.dct:
                return self.dct[n]
            else:
                val = self.climbStairs(n-1) + self.climbStairs(n-2)

        self.dct[n] = val

        return val


obj = Solution()
print(obj.climbStairs(100))
