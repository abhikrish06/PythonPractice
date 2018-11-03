import math

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def distance(p1, p2):
            return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

        max_area, area = 0.0, 0.0
        for i in range(len(points)-2):
            for j in range(i+1, len(points)-1):
                for k in range(i+2, len(points)):
                # print(points[i],points[j], points[j+1])
                # x1, y1 = points[i][0], points[i][1]
                # x2, y2 = points[j][0], points[j][1]
                # x3, y3 = points[j+1][0], points[j+1][1]
                    a = points[i]
                    b = points[j]
                    c = points[k]
                    # print(a, b, c)
                    side_a = distance(a, b)
                    side_b = distance(b, c)
                    side_c = distance(c, a)
                    s = 0.5 * (side_a + side_b + side_c)
                    area = math.sqrt(s * abs(s - side_a) * abs(s - side_b) * abs(s - side_c))
                    print('area:', area)
                    max_area = max(max_area,area)
        return max_area

obj = Solution()
#print(obj.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
#print(obj.largestTriangleArea([[9,0],[0,2],[3,1],[10,8]]))


print(obj.largestTriangleArea([[-35,19],[40,19],[27,-20],[35,-3],[44,20],[22,-21],[35,33],[-19,42],[11,47],[11,37]]))