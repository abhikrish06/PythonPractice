class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        tm = [float(target - pos)/sp for pos, sp in sorted(zip(position, speed))]
        cntr, cur_tm = 0, 0
        for i in tm[::-1]:
            if i > cur_tm:
                cntr += 1
                cur_tm = i

        return cntr


obj = Solution()
print('answer: ', obj.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
print('answer: ', obj.carFleet(target=10, position=[2, 4], speed=[3, 2]))
