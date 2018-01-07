import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

arr_sm_hr = []
max_sum = -65230
for i in range(4):
    for j in range(4):
        arr_sum = 0
        arr_sm_hr = []
        arr_sm_hr.append(arr[i][j])
        arr_sm_hr.append(arr[i][j+1])
        arr_sm_hr.append(arr[i][j+2])
        arr_sm_hr.append(arr[i+1][j+1])
        arr_sm_hr.append(arr[i+2][j])
        arr_sm_hr.append(arr[i+2][j+1])
        arr_sm_hr.append(arr[i+2][j+2])
        arr_sum = sum(arr_sm_hr)
        print(arr_sum, max_sum)
        if arr_sum > max_sum:
            max_sum = arr_sum
print(max_sum)

# simpler soln
res = []

for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
        res.append(s)

print(max(res))