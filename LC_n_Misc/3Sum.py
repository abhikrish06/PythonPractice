def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    print(nums)
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i+1]:
            continue
        for j in range(len(nums)-2):
            s = nums[i] + nums[j + 1] + nums[j + 2]
            if s == 0:
                res.append([nums[i], nums[j + 1], nums[j + 2]])
    noDupes = []
    [noDupes.append(i) for i in res if not noDupes.count(i)]
    return noDupes

print(threeSum([-1, 0, 1, 2, -1, -4]))
#print(threeSum([0,0,0,0,0,0]))
#print(threeSum([-1,0,1,0]))
#nums = [-1, 0, 1, 2, -1, -4]

nums = [0,0,0,0]
nums.sort()
res = []
#print(nums)
for i in range(len(nums)-2):
    j = i+1
    k = len(nums) - 1
    if i > 0 and nums[i] == nums[i-1]:
        continue
    while j < k:
        if j > i + 1 and nums[j] == nums[j - 1]:
            j += 1
            continue
        total = nums[i] + nums[j] + nums[k]
        if total > 0:
            k -= 1
        else:
            if total == 0:
                res.append([nums[i], nums[j], nums[k]])
            j += 1
print(res)