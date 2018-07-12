# class Solution:
#     def reorderLogFile(self, logFileSize, logLines):
#         for

logFileSize = int(input())
logLines = []
cntr = 0

for i in range(logFileSize):
    tmp = list(input().split(' '))
    if tmp[1].isnumeric():
        logLines.append(tmp)
        cntr += 1
    else:
        logLines.insert(0, tmp)

print(logLines)
res = []
for i in range(cntr-1):
    l1, l2 = len(logLines[i]), len(logLines[i+1])
    n = min(l1,l2)
    for j in range(n):
        if logLines[i][j+1].lower() == logLines[i+1][j+1].lower():
            continue
        else:
            continue

# 5
# a1 9 3 2 1
# g1 Act car
# zo4 4 7
# ab1 off KEY
# a8 act zoo

