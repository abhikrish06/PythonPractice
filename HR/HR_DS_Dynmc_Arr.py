N, Q = map(int, input().split())
seqList = [[] for i in range(N)]
lastAnswer = 0
print(seqList)
for i in range(Q):
    print('i: ', i)
    temp = list(map(int, input().split()))
    print(temp)
    if temp[0] == 1:  # type 1 query
        seq = (temp[1] ^ lastAnswer) % N
        # print('seq: ', seq)
        # print('seqList[seq]: ', seqList[seq])
        seqList[seq].append(temp[2])
        print('seqList: ', seqList)
    elif temp[0] == 2:  # type 2 query
        seq = (temp[1] ^ lastAnswer) % N
        print('seq: ', seq)
        val = temp[2] % len(seqList[seq])
        lastAnswer = seqList[seq][val]
        print('lastAnswer :' , lastAnswer)

# 2 5
# 1 0 5
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1