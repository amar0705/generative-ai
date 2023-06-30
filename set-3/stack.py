from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        # Add the item to the first queue
        self.q1.put(item)

    def pop(self):
        # Move all items except the last one from q1 to q2
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        # Remove and return the last item from q1
        if not self.q1.empty():
            popped_item = self.q1.get()

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return popped_item

# Test the stack implementation
stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())
print(stack.pop())
