def answer(total_lambs):
    gen_stingy_arr = [gen_dist(total_lambs), stingy_dist(total_lambs)]
    return max(gen_stingy_arr) - min(gen_stingy_arr)

def gen_dist(total_lambs):
    val = 1
    while True:
        total = (2 ** val) - 1
        if total <= total_lambs:
            val += 1
        else:
            val -= 1
            break
    return val

def stingy_dist(total_lambs):
    val = 1
    while True:
        total = (fibonacci(val + 2) - 1)
        if total <= total_lambs:
            val += 1
        else:
            val -= 1
            break
    return val

def fibonacci(n):
    a, b = 1, 1
    for i in range(1, n-1):
        a, b = b, a + b

    return b

#print(fibonacci(6))
print(answer(10))
print(answer(143))