import numpy as np
def matsum(mat):
    rows = len(mat)
    cols = len(mat[0])
    print(rows, cols)
    # val = [[0] * cols] * rows
    val = np.zeros([rows,cols], int)
    print(val)
    # for i in range(rows):
    #     for j in range(cols):
    #         print(mat[i][j], end=' ')
    #     print()

    for i in range(rows):
        for j in range(cols):
            frst, lft, mid = 0, 0, 0
            # print(frst,lft,mid)
            if i - 1 >= 0:
                frst = mat[i - 1][j]

            if j - 1 >= 0:
                lft = mat[i][j - 1]

            if j - 1 >= 0 and i - 1 >= 0:
                mid = mat[i - 1][j - 1]

            val[i][j] = mat[i][j] - frst - lft + mid
            print(val)

            # val[i][j] += lft + mat[i][j]
            # if i - 1 >= 0:
            #     for k in range(cols):
            #         val[i][k] += val[i - 1][k]
    return val


mat = [[1, 2, 3], [1, 1, 4], [3, 7, 11]]
print(matsum(mat))
