def zro_mat(ip_mat):
    n = len(ip_mat)
    m = len(ip_mat[0])
    rowlst, collst = [], []
    for i in range(n):
        for j in range(m):
            if ip_mat[i][j] == 0:
                rowlst.append(i)
                collst.append(j)
                break
    # print(rowlst)
    # print(collst)
    for i in rowlst:
        for j in range(m):
            ip_mat[i][j] = 0
    # print(ip_mat)
    for i in collst:
        for j in range(n):
            ip_mat[j][i] = 0
    return ip_mat

if __name__ == '__main__':
    #n = int(input())
    ip_mat = [[1, 0, 3], [4, 5, 6], [7, 8, 9]]
    print(ip_mat)
    #mat_rotate(ip_mat)
    print(zro_mat(ip_mat))