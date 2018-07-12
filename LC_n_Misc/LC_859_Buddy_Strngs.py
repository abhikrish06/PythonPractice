class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        cntr = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                cntr += 1

        if cntr > 2 or cntr == 1:
            return False
        elif cntr == 2:
            return set(A) == set(B)
        else:
            return len(set(A)) != len(A)

obj = Solution()
print(obj.buddyStrings('ab', 'ab'))
print(obj.buddyStrings('ab', 'ba'))
print(obj.buddyStrings('aa', 'aa'))
print(obj.buddyStrings(A="aaaaaaabc", B="aaaaaaacb"))
print(obj.buddyStrings(A="abab", B="abab"))
