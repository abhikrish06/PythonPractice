# a = [1, 2, 3]  # input array
# sm = 0  # result
# for idx, val in enumerate(a):
#     print(idx,val)
#     sm += val * (idx + 1) * (len(a) - idx)
# print(sm) # 27=result of [1], [3], [4], [1, 3], [3, 4], [1, 3, 4]
#
# arr = [1,2,3]
# res = 0
# for i in range(len(arr)):
#     print(arr[i])
#     res += (arr[i] * (i+1) * (len(arr) - i))
#
# print('res', res)
#
#
# dct = {'a':1, 'b':2, 'c':3}
# dct2 = {'a':1, 'b':5, 'd':3}
# print({**dct, **dct2})
#
# a = [1,2,3]
# b = a
# c = [1,2,3]
#
# print(a==b)
# print(a is b)
# print(a==c)
# print(a is c)
#
# print({True:'yse', 1:'no', 1.0:'maybe'})
#
# s = 'hackerrank'
# dct = {}
# for i in range(len(s)):
#     if s[i] in dct:
#         dct[s[i]].append(i)
#     else:
#         dct[s[i]] = [i]
#
# print(dct)

matrix = [[0 for i in range(4)] for j in range(4)]
print(matrix)
for i in range(4):
    for j in range(4):
        matrix[i][j] = i*4 + j
print(matrix)

