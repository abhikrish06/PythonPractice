import math
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    scr_lst = []
    sum = 0
    for _ in range(n):
        score = int(input())
        scr_lst.append(score)
    #print(scr_lst)
    for i in range(n):
        sum = sum + scr_lst[i]
    print("mean: ", sum/n)

    scr_lst.sort()
    #print(scr_lst)
    if n%2 == 0:
        print("median:", (scr_lst[(n//2)-1]+scr_lst[(n//2)])/2)
    else:
        p = math.floor(n / 2)
        print("median:", scr_lst[p])

    #print(Counter(scr_lst))
    mode_dict = dict((x,scr_lst.count(x)) for x in set(scr_lst))
    #print(mode_dict)
    v = list(mode_dict.values())
    k = list(mode_dict.keys())
