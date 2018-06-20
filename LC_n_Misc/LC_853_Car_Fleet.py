# incorrect
# incomplete

class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        list3 = [a + b for a, b in zip(position, speed) if a + b <= target]
        # print(list3)
        set_list3 = set(list3)

        return len(set_list3)


obj = Solution()
print('answer: ', obj.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
print('answer: ', obj.carFleet(target=10, position=[2, 4], speed=[3, 2]))
