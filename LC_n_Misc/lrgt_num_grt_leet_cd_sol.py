def dominantIndex(nums):
    largest = max(nums)
    return nums.index(largest) if all([largest == num or num * 2 <= largest for num in nums]) else -1

#print(dominantIndex([1, 3, 0, 6]))
#print(dominantIndex([1, 2, 3, 4]))
#print(dominantIndex([0, 0, 0, 1]))
#print(dominantIndex([0,0,3,2]))