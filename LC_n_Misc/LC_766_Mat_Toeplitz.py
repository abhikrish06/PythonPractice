class Solution:
    def isToeplitzMatrix(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row-1):
            for j in range(col-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

obj = Solution()
print(obj.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print((obj.isToeplitzMatrix([[1,2],[2,2]])))