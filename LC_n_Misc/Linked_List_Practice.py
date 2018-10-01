class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head

        if position < 0:
            return None

        for i in range(1, position):
            current = current.next
        return current

    def insert(self, element, position):
        if position < 1:
            return self.head

        current = self.head

        if position == 1:
            element.next = current
            self.head = element

        if position > 1:
            for i in range(1, position-1):
                current = current.next
            element.next = current.next
            current.next = element


    def delete(self, value):
        prev = None
        current = self.head

        while current.value != value and current.next:
            prev = current
            current = current.next

        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def insert_first(self, element):
        element.next = self.head
        self.head = element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            current = deleted_element.next
            self.head = current
            return deleted_element
        else:
            return None

class Stack(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
# print(ll.get_position(1).value)
# print(ll.get_position(2).value)
print(ll.get_position(3).value)
# print(ll.get_position(4).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
# print(ll.get_position(1).value)
# print(ll.get_position(2).value)
print(ll.get_position(3).value)
# print(ll.get_position(4).value)

# Test delete
ll.delete(1)
# Should print 2 now
print('delete')
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)


# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print('stack starts')
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
