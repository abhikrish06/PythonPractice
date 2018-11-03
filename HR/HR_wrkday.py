# Complete the function below.

def minimumMoves(a, m):
    if len(a) != len(m):
        return 0
    moves = 0
    for i in range(len(a)):
        for j in range(len(str(a[i]))):
            str_a = str(a[i])
            str_m = str(m[i])
            if str_a[j] == str_m[j]:
                continue
            else:
                cntr = int(str_a[j]) - int(str_m[j])
                if cntr < 0:
                    moves += (-1) * cntr
                else:
                    moves += cntr
    return moves


print(minimumMoves([123,123], [234, 245]))