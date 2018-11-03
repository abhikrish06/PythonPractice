import math

def cal_med(num):
    #print(num)
    n = len(num)
    if n % 2 == 0:
        return (int(num[(n // 2) - 1]) + int(num[(n // 2)])) / 2
    else:
        p = math.floor(n / 2)
        return int(num[p])

if __name__ == '__main__':
    #numbers = []
    #frequency = []
    final_list = []
    n = int(input())
    k = 0
    numbers = list(map(int, input().split()))
    frequency = list(map(int, input().split()))
    # print("numbers:", numbers)
    # print("frequency:", frequency)
    for i in numbers:
        for j in range(frequency[k]):
            final_list.append(i)
        k += 1
    # print(final_list)
    nums = sorted(final_list)
    # print(final_list)
    n1 = len(nums)
    q1 = cal_med(nums[:n1//2])
    if n1 % 2 == 0:
        q3 = cal_med(nums[n1//2:])
    else:
        q3 = cal_med(nums[n1//2 + 1:])
    print('%.1f' % (q3 - q1))