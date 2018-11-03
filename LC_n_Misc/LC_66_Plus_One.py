class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        val = int(''.join(map(str, digits)))
        print(val)
        val += 1
        return [int(i) for i in str(val)]


obj = Solution()
print(obj.plusOne([0]))
