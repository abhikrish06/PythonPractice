# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def count_days(A):
    set_A = set()
    strt, end = 0, 0
    set_A.add(A[0])
    #print('bef set', set_A)

    for i in range(1,len(A)): # [2,1,1,3,2,1,1,3]
        if A[i] == A[strt]:
            while (strt < i and A[strt] == A[i]):  # checking continuous same destinations
                strt += 1
            end += 1
        else:
            if A[i] not in set_A:
                set_A.add(A[i])
                end = i
            # print(set_A, end)
    #print(strt, end)
    return end - strt + 1


def solution(A):
    # write your code in Python 3.6
    # tot_des = len(set(A)) # total distinct destinations
    #rev_A = A[::-1]

    cntA = count_days(A)
    return cntA
    #cnt_revA = count_days(rev_A)

    # if cntA > cnt_revA:
    #     return cnt_revA
    # else:
    #     return cntA

if __name__ == "__main__":
    result = solution([2,1,1,3,2,1,1,3,1,1,1,2,5])  #[2,1,1,3,2,1,1,3], [7,3,7,3,1,3,4,1]
    print(result)