class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        # print(a)
    def computeDifference(self):
        n = len(self.__elements)
        print(n)
        print(a)
        for i in range(n - 1):
            for j in range(i+1, n):
                diff = abs(a[i] - a[j])
            #print(diff, self.maximumDifference)
                if diff > self.maximumDifference:
                    self.maximumDifference = diff
        return self.maximumDifference

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)