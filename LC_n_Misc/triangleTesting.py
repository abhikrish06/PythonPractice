# Return whether the triangle is isosceles, equilateral or  not a triangle from given sides

def triangleTesting(a,b,c):
    if a < 0 or b < 0 or c < 0:
        return "negative edge weights, not a triangle"
    elif a+b <= c or b+c <= a or c+a <= b:
        return "not a triangle"
    elif a == b and b == c:
        return "Triangle is equilateral"
    elif a == b or b == c or c == a:
        return "triangle is isosceles"
    else:
        return "Triangle is scalene"

print(triangleTesting(1,2,3))
print(triangleTesting(2,3,4))
print(triangleTesting(2,2,3))
print(triangleTesting(3,3,3))
print(triangleTesting(0,0,0))
print(triangleTesting(1,-3,-4))

