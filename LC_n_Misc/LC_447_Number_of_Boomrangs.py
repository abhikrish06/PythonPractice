import collections
class Solution:
    def distance(self, a, b):
        x = a[0] - b[0]
        y = a[1] - b[1]

        return x * x + y * y

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dct = collections.Counter()
        res = 0
        for i in range(len(points)):
            dct.clear()
            for j in range(len(points)):
                if i == j:
                    continue
                dist = self.distance(points[i], points[j])
                dct[dist] += 1

            for val in dct.values():
                res += (val * (val-1))
        return res

obj = Solution()
print(obj.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
