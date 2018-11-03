from itertools import combinations,chain

if __name__ == '__main__':
    S, k = input().split()
    new_S = sorted(list(S))
    for i in range(int(k)):
        final = list(combinations(new_S, int(i + 1)))
        #final = list(chain.from_iterable(combinations(new_S, int(i + 1))))
        for j in range(len(final)):
           print("".join(final[j]))
        #print(final)

# print(list(combinations('12345',1)))
