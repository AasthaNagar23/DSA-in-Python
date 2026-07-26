class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Enqueue
    def enqueue(self, data):
        self.stack1.append(data)

    # Dequeue
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"

        # Transfer only when stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    # Front element
    def front(self):
        if self.is_empty():
            return "Queue is Empty"

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    # Check if queue is empty
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    # Size
    def size(self):
        return len(self.stack1) + len(self.stack2)

    # Display queue
    def display(self):
        print(self.stack2[::-1] + self.stack1)


# Driver Code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front:", q.front())
print("Dequeued:", q.dequeue())

q.display()

print("Size:", q.size())