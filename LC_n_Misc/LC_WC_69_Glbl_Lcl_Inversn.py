class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        cntr_G, cntr_L = 0, 0
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                cntr_L += 1

        #print(cntr_L)

obj = Solution()
obj.isIdealPermutation([1,0,2])