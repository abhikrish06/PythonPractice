class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        if n == 0:
            return 0

        l, r = 0, n - 1
        cnt = 0
        print(l, r)

        while l < r and height[l] <= 0:
            l += 1
        print(l)

        while l < r and height[r] < height[r - 1]:
            r -= 1
        print(r)

        for i in range(r, l, -1):
            if height[i] > height[i - 1]:
                print('r:', i)
                cnt += (height[i] - height[i - 1])
        return cnt

obj = Solution()
# print(obj.trap([]))
# print(obj.trap([0]))
print(obj.trap([2,1,0,2]))
