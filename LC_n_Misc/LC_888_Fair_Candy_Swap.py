class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)

        dif = (sumA - sumB)//2

        A = set(A)

        for b in set(B):
            if dif+b in A:
                return [dif+b, b]

obj = Solution()
print(obj.fairCandySwap([1,1],[2,2]))
print(obj.fairCandySwap([1,2],[2,3]))
print(obj.fairCandySwap([1,2,5],[2,4]))
