if __name__ == '__main__':
    number = []
    weight = []
    tot_sum = 0
    sum_wt = 0
    n = int(input())
    # for _ in range(int(input())):
    number = input().split()
    weight = input().split()

    for i in range(n):
        sum_wt = sum_wt + int(weight[i])
        tot_sum = tot_sum + int(number[i]) * int(weight[i])

        # print(number[i], weight[i])

    # print(number)
    # print(weight)
    print('%.1f' % (tot_sum/sum_wt))