class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s1,t1 = [],[]
        for ch in S:
            if ch.isalpha():
                s1.append(ch)
            else:
                if len(s1) > 0:
                    s1.pop()
        print(s1)

        for ch in T:
            if ch.isalpha():
                t1.append(ch)
            else:
                if len(t1) > 0:
                    t1.pop()
        print(t1)
        return s1 == t1


obj = Solution()
print(obj.backspaceCompare(S="a##c", T="#a#c"))
print(obj.backspaceCompare(S = "a#c", T = "b"))
print(obj.backspaceCompare(S = "ab##", T = "c#d#"))
print(obj.backspaceCompare(S = "ab#c", T = "ad#c"))