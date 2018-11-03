# Largest Number Greater Than Twice of Others

def lrgt_num_gtr(nums):
    #nums.sort()
    #print(nums)
    max_num = max(nums)
    print(max_num)
    for i in range(len(nums)):
        val = 2 * nums[i]
        print("val: ", val)
        if max_num >= val:
            print("in IF")
            continue
        elif max_num == nums[i]:
            print("in ELIF")
            continue
        else:
            print("in Else")
            return -1
    return nums.index(max_num)

#print(lrgt_num_gtr([1, 3, 0, 6]))
#print(lrgt_num_gtr([1, 2, 3, 4]))
#print(lrgt_num_gtr([0, 0, 0, 1]))
print(lrgt_num_gtr([0,0,3,2]))