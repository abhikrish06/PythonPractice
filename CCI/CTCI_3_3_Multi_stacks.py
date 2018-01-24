class MultiStack():
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()

        if len(self.stacks) == 0:
            return None
        items = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return items

    def pop_at(self, stacknumber):
        if stacknumber < 0 or len(self.stacks) <= stacknumber or len(self.stacks[stacknumber]) == 0:
            return None
        return self.stacks[stacknumber].pop()
    