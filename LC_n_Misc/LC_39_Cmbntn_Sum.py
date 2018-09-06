class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []

        def hlpr(curr_target, stk):
            if curr_target <= 0:
                res.append(stk)
                return

            for c in candidates:
                if c > curr_target:
                    break
                elif not stk or c >= stk[-1]:
                    hlpr(curr_target-c, stk+[c])


        # for c in candidates:
        #     diff, cntr = target, 0
        #     while diff >= 0:
        #         cntr += 1
        #         diff = diff - c
        #         if diff in candidates:
        #             tmp_ar = [c] * cntr
        #             tmp_ar.append(diff)
        #             if sorted(tmp_ar) not in res:
        #                 res.append(sorted(tmp_ar))
        hlpr(target, [])

        return res


obj = Solution()
print(obj.combinationSum(candidates=[2, 3, 6, 7], target=7))
print(obj.combinationSum(candidates=[2, 3, 5], target=8))
print(obj.combinationSum(candidates=[2, 3, 7], target=18))
# [[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,2,3,7],[2,2,2,3,3,3,3],[2,2,7,7],[2,3,3,3,7],[3,3,3,3,3,3]]
