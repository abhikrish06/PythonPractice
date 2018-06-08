class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        i, j = 0, len(s)-1
        lst_s = list(s)
        while True:
            if lst_s[i] == lst_s[j]:
                i += 1
                j -= 1
                print(i,j)
                continue
            else:
                break
        print('out: ', i, j)

        s1 = lst_s[:i]+lst_s[i+1:]
        s2 = lst_s[:j]+lst_s[j+1:]

        print('s1:',s1,'s2:', s2)
        if s1 == s1[::-1] or s2 == s2[::-1]:
            return True
        else:
            return False


obj = Solution()
# print(obj.validPalindrome('abca'))
print(obj.validPalindrome('abcda'))