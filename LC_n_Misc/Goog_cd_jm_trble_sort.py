t = int(input())

def troubleSort(lst):
    val = False
    while not val:
        val = True
        for i in range(len(lst)- 2):
            if lst[i]>lst[i+2]:
                val = False
                lst[i], lst[i + 2] = lst[i+2], lst[i]
    return lst

def testTroubleSort(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return i
    return -1

for i in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    trbl_srt_lst = troubleSort(lst)
    vldtn = testTroubleSort(trbl_srt_lst)

    if vldtn == -1:
        print('Case #%i: %s' %(i, 'OK'))
    else:
        print('Case #%i: %i' % (i, vldtn))
