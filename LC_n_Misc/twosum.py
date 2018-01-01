def twoSum(self, nums, target):
	outlst = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sumtrgt = nums[i]+nums[j]
            if (sumtrgt == target):
                outlst.append(nums[i],nums[j])
            else:
                continue
    
    return(outlst);