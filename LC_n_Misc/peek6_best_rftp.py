# incomplete
def bestrooftop(radius, eventsgrid):
    dct = {}
    for i in range(len(eventsgrid)):
        x,y = eventsgrid[i][0], eventsgrid[i][1]
        cumu_h = 0.0
        for j in range(len(eventsgrid)):
            x1, y1 = eventsgrid[j][0], eventsgrid[j][1]
            w1 = eventsgrid[j][2]

            d = 1 + ((x-x1)**2 + (y-y1)**2)**0.5
            if d <= radius:
                h = w1/d
                cumu_h += h


    return dct

# 4
# 3
# 3
# 0 0 1
# 1 1 2
# 2 2 1

print(bestrooftop(3, [[0,0,1], [1,1,2], [2,2,1]]))