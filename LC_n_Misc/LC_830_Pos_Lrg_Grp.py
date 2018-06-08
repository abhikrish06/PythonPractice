class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res, in_res = [], []
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                in_res.append(i)
                in_res.append(i+1)
                # print(in_res)
            else:
                if len(in_res) >= 3: res.append([in_res[0], in_res[-1]])
                in_res = []
        if len(in_res)>= 3: res.append([in_res[0],in_res[-1]])
        return res

obj = Solution()
print(obj.largeGroupPositions('abbxxxxzzy'))
print(obj.largeGroupPositions('abc'))
print(obj.largeGroupPositions('abcdddeeeeaabbbcd'))
print(obj.largeGroupPositions('aaa'))


s ="ASDF"
n = s.index('S')
print(n)