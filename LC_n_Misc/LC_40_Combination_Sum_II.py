# incomplete
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates = sorted(candidates)
        res = []

        for i in range(len(candidates)-1):
            if candidates[i] == target:
                res.append(candidates[i])
                return res

            if candidates[i] > target:
                return res

            tmp_c = candidates[i+1:]
            ar = []
            for j in range(len(tmp_c)):
                ar.append(candidates[i])
                ar.append(tmp_c[j])





obj = Solution()
print(obj.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))