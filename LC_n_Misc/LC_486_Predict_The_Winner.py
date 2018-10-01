class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        mat = [[-1 for i in range(n)] for j in range(n)]

        def predictor(start, end, turn):
            if mat[start][end] == -1:
                r = 0
                if start == end:
                    r =  nums[start] if turn else 0
                else:
                    if turn:
                        r = max(nums[start]+predictor(start+1, end, False), nums[end]+predictor(start, end-1, False))
                    else:
                        r = min(predictor(start+1, end, True), predictor(start, end-1, True))
                mat[start][end] = r
            return mat[start][end]

        return 2*(predictor(0, n-1, True)) >= sum(nums)

obj = Solution()
print(obj.PredictTheWinner([1,5,2]))
print(obj.PredictTheWinner([1,5,23,7]))