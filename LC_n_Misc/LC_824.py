class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vow = 'aeiouAEIOU'
        con = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        lst_s = S.split()
        # print(lst_s)

        for i in range(len(lst_s)):
            if lst_s[i][0] in vow:
                lst_s[i] = lst_s[i]+'ma'
                lst_s[i] = lst_s[i] + 'a' * (i + 1)
            elif lst_s[i][0] in con:
                vl = lst_s[i][0]
                lst_s[i] = lst_s[i][1:] + (vl)
                lst_s[i] = lst_s[i] + 'ma'
                lst_s[i] = lst_s[i] + 'a' * (i + 1)
        return " ".join(lst_s)


obj = Solution()
print(obj.toGoatLatin("I speak Goat Latin"))
print(obj.toGoatLatin("The quick brown fox jumped over the lazy dog"))
