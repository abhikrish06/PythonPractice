#!/bin/python3

import sys


def checkAll(n, height, position):
    # Complete this function
    zip_h_p = list(zip(position,height))
    # print(list(zip_h_p))
    res, resl, resr = "", "", ""
    for i in range(len(zip_h_p)-1):
        if zip_h_p[i][0] + zip_h_p[i][1] >= zip_h_p[i+1][0]:
            for j in range(i+1, len(zip_h_p)-1):
                if zip_h_p[i][0] + zip_h_p[i][1] >= zip_h_p[j][0]:
                    resl = "LEFT"
                else:
                    break
        else:
            resl = "NONE"
            break

    for i in range(len(zip_h_p)-1,0,-1):
        if zip_h_p[i][0] - zip_h_p[i][1] <= zip_h_p[i-1][0]:
            for j in range(i-1, 0, -1):
                if zip_h_p[i][0] - zip_h_p[i][1] <= zip_h_p[j][0]:
                    resr = "RIGHT"
                else:
                    break
        else:
            resr = "NONE"
            break

    if resl == "NONE" and resr == "NONE":
        res = "NONE"
    elif resl == "LEFT" and resr == "NONE":
        res = "LEFT"
    elif resl == "NONE" and resr == "RIGHT":
        res = "RIGHT"
    elif resl == "LEFT" and resr == "RIGHT":
        res = "BOTH"

    return res

if __name__ == "__main__":
    n = int(input().strip())
    position = list(map(int, input().strip().split(' ')))
    height = list(map(int, input().strip().split(' ')))
    ret = checkAll(n, height, position)
    print(ret)

# many test cases failed
