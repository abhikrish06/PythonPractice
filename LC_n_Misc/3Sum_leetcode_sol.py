def threeSum(nums):
    res = []
    nums.sort()
    print(nums)
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        print("l: ", l, "r: ", r)
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            print("s: ", s)
            if s < 0:
                l += 1
                print("l: ", l)
            elif s > 0:
                r -= 1
                print("r: ", r)
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
                print("after l: ", l, "r: ", r)
    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))
#print(threeSum([0,0,0,0,0,0]))
#print(threeSum([-1,0,1,0]))