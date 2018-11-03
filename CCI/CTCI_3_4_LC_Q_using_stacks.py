class MyQueue:
    def __init__(self):
        self.stck = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stck.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stck) == 0:
            return None
        else:
            return self.stck.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stck) == 0:
            return None
        else:
            return self.stck[0]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stck) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(-1)
print(obj.pop())
print(obj.peek())
print(obj.empty())