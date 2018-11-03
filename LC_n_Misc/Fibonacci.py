# def fibonacci(n):
#     curr = 1
#     prev = 0
#     counter = 0
#     while counter < n:
#         yield curr
#         prev, curr = curr, prev + curr
#         counter += 1


class fibonacciCalculate:

    def __init__(self, n):
        self.n = n
        self.fib = [-1] * (n+1)

    def fibonacci(self, n):

        if n == 0 or n == 1:
            val = 1
        else:
            if self.fib[n] > 0:
                return self.fib[n]
            else:
                val = self.fibonacci(n-1) + self.fibonacci(n-2)
        self.fib[n] = val
        return val

obj = fibonacciCalculate(7)
print(obj.fibonacci(7))

# fib_dct = {}
#
# def fibonacci(n):
#     if n in fib_dct:
#         return fib_dct[n]
#
#     if n == 0:
#         val = 0
#     elif n == 1:
#         val = 1
#     elif n >= 2:
#         val = fibonacci(n-1) + fibonacci(n-2)
#
#     fib_dct[n] = val
#
#     return val
#
# print(fibonacci(5))
# print(fibonacci(100))
