#incomplete

from collections import defaultdict

class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        d = defaultdict(list)

        for a,b in dislikes:
            d[a].append(b)

        print(d)

        return True

obj =Solution()

print(obj.possibleBipartition(4, [[1,2],[1,3],[2,4]]))
print(11//2)