class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for l in range(len(height) - 1):
            for b in range(l + 1, height, 1):
                intr_area = min(height[l], height[b]) * (b - l)
                if intr_area > max_area:
                    max_area = intr_area

                else:
                    continue
