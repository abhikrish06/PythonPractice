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
#for i in range(len(nums)-2):
#    print(nums[i] + nums[i + 1] + nums[i + 2])