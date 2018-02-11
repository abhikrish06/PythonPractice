def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr, prev + curr
        counter += 1