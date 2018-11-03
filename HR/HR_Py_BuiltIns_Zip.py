n, x = map(int, input().split())
marks = []
for i in range(x):
    marks.append(map(float,input().split()))

for i in zip(*marks):
    print(sum(i)/len(i))