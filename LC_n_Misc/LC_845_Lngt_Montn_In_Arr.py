class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = []
        i,= 0
        bol = True
        while bol:
            while (A[i] < A[i+1]):
                pass
