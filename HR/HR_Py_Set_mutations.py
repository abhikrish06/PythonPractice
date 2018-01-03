A = int(input())
set_A = set(input().split())
N = int(input())
for i in range(N):
    oper = input().split()[0]
    set_B = set(input().split())
    # print(set_B)
    eval('set_A.' + oper + '(set_B)')
    #print(set_A)
print(sum(map(int, set_A)))



# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 1
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11