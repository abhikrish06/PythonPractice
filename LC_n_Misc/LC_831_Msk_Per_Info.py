class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        num = '1234567890'
        val = []
        if '@' in S:
            v = S.index('@')
            return S[0].lower()+'*****'+S[v-1].lower()+S[v:].lower()
        for i in S:
            if i in num:
                val.append(i)
        if len(val) == 10:
            return '***-***-'+ ''.join(val[6:])
        elif len(val) == 11:
            return '+*-***-***-' + ''.join(val[7:])
        elif len(val) == 12:
            return '+**-***-***-' + ''.join(val[8:])
        elif len(val) == 13:
            return '+***-***-***-' + ''.join(val[7:])


obj = Solution()
print(obj.maskPII('LeetCode@LeetCode.com'))
print(obj.maskPII('AB@qq.com'))
print(obj.maskPII('1(234)567-890'))
print(obj.maskPII('86-(10)12345678'))