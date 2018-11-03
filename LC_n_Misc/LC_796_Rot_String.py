class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        cnt = 0

        for i in range(len(A)):
            temp = A[:i + 1]
            temp2 = A[i + 1:]
            #print(temp2+temp)
            #print(temp2.extend(temp))
            if B == temp2+temp:
                cnt += 1
            else:
                continue

        if cnt > 0:
            return True
        else:
            return False

obj = Solution()
print(obj.rotateString("abcde", "cdeab"))