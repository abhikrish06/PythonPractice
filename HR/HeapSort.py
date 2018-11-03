import heapq
def heapsort(iterable):
    h = []
    for i in iterable:
        heapq.heappush(h, i)
    return [heapq.heappop(h) for _ in range(len(h))]


print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))