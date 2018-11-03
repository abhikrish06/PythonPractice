import unittest


def mat_rotate(ip_mat):
    n = len(ip_mat[0])
    emp_mat = [[0 for r in range(n)] for c in range(n)]
    # print(emp_mat)
    l = n - 1
    for i in range(n):
        k = 0
        for j in range(n):
            emp_mat[i][j] = ip_mat[k][l]
            k += 1
        l -= 1
    return emp_mat
    # print(ip_mat)


def mat_rotate_inplace(ip_mat):
    n = len(ip_mat[0])
    l = n - 1
    for i in range(n):
        k = 0
        for j in range(n):

            k += 1
        l -= 1

    return ip_mat
    # print(ip_mat)


class Test(unittest.TestCase):
    # def test_rotate_matrix(self):
    #     mat1 = [[1, 2], [3, 4]]
    #     mat2 = [[2, 4], [1, 3]]
    #     self.assertEqual(mat_rotate(mat1), mat2)
    #     mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #     mat4 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    #     self.assertEqual(mat_rotate(mat3), mat4)
    #     mat5 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    #     mat6 = [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
    #     self.assertEqual(mat_rotate(mat5), mat6)

    def test_rotate_matrix_in_place(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[2, 4], [1, 3]]
        mat_rotate_inplace(mat1)
        self.assertEqual(mat1, mat2)
        mat3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        mat4 = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        mat_rotate_inplace(mat3)
        self.assertEqual(mat3, mat4)
        mat5 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        mat6 = [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]
        mat_rotate_inplace(mat5)
        self.assertEqual(mat5, mat6)


# if __name__ == "__main__":
#     unittest.main()

if __name__ == '__main__':
    n = int(input())
    ip_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(ip_mat)
    #mat_rotate(ip_mat)
    print(mat_rotate_inplace(ip_mat))
