class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items) - 1]
        return None

    def size(self):
        return len(self.items)

class SortStack():
    def __init__(self):
        self.stck = Stack()
        self.temp_stck = Stack()

    def is_empty(self):
        return self.stck == []

    def push(self,item):
        if self.stck.is_empty() or item < self.stck.peek():
            self.stck.push(item)
        else:
            while self.stck.peek() is not None and item > self.stck.peek():
                self.temp_stck.push(self.stck.pop())
            self.stck.push(item)
            while not self.temp_stck.is_empty():
                self.stck.push(self.temp_stck.pop())
    def pop(self):
        return self.stck.pop()

    def peek(self):
        if not self.stck.is_empty():
            return self.stck[-1]
        return None