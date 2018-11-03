class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])

# Your NumArray object will be instantiated and called as such:
obj = NumArray([[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]])
param_1 = obj.sumRange(i,j)