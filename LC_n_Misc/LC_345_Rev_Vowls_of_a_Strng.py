class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        lst_s = list(s)
        i, j = 0, len(s)-1
        while i<j:
            if lst_s[i] in vowels:
                if lst_s[j] in vowels:
                    lst_s[i], lst_s[j] = lst_s[j], lst_s[i]
                    j -= 1
                    i += 1
                else:
                    j -= 1
            else:
                i += 1

        return ''.join(lst_s)


obj = Solution()
print(obj.reverseVowels('hello'))
print(obj.reverseVowels('leetcode'))
print(obj.reverseVowels('lol'))
print(obj.reverseVowels('leela'))
print(obj.reverseVowels('aA'))
