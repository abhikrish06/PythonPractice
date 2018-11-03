def solution(A, B):
    # write your code in Python 3.6
    cnt = 0
    d = {'A':14, 'K':13, 'Q':12, 'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2}
    for i in range(len(A)):
        if d[A[i]] > d[B[i]]:
            cnt += 1
    return cnt
if __name__ == "__main__":
    result = solution('A586QK','JJ653K')
    print(result)