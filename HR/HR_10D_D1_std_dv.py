import statistics, math

if __name__ == '__main__':
    n = int(input())
    sum_val = 0
    numbers = map(int, input().split())
    nums = sorted(numbers)
    # print("numbers: ", nums)
    u = statistics.mean(nums)
    for i in nums:
        sum_val = sum_val + (i - u)**2
    std_dev = math.sqrt(sum_val/n)
    print('%.1f' % std_dev)
