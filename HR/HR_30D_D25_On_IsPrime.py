def isPrime(p):
    if p == 1 or p == 2:
        return 'Prime'
    else:
        for i in range(2, int(p**0.5)+1):
            if p % i == 0:
                return 'Not prime'
        return 'Prime'

T = int(input())
for i in range(T):
    print(isPrime(int(input())))
