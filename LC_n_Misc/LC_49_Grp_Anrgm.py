# class Solution:
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         res, temp = [], []
#         for i in range(len(strs)):
#             temp2 = []
#             if strs[i] not in temp:
#                 # print('inside:', i)
#                 temp.append(strs[i])
#                 temp2.append(strs[i])
#             else:
#                 # print(i)
#                 continue
#             for j in range(i + 1, len(strs) - 1):
#                 if self.chk_anagram(strs[i], strs[j]):
#                     temp.append(strs[j])
#                     temp2.append(strs[j])
#             res.append(temp2)
#         return res
#
#     def chk_anagram(self, s1, s2):
#         lst_S1 = sorted(list(s1))
#         lst_S2 = sorted(list(s2))
#         return lst_S1 == lst_S2


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            # print(sorted_x)
            if sorted_x in d:
                d[sorted_x].append(x)
            else:
                d[sorted_x] = [x]
            print(d)
        return [v for v in d.values()]

obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(obj.groupAnagrams(["", ""]))
