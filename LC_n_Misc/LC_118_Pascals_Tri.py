class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]

        res = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            temp = [1]
            # print(res)
            val = res[-1]
            print('val:', val)
            # sm = 0
            for j in range(len(val) - 1):
                # print(val[j:j + 2])
                sm = sum(val[j:j + 2])
                # print(sm)
                temp.append(sm)
            temp.append(1)
            res.append(temp)

        return res


obj = Solution()
print(obj.generate(6))
