from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Insert element
    def enqueue(self, value):
        self.queue.append(value)

    # Remove front element
    def dequeue(self):
        if (self.queue==0):
            return "Queue is Empty"
        return self.queue.popleft()

    # Return front element
    def front(self):
        if (self.queue==0):
            return "Queue is Empty"
        return self.queue[0]

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Return size
    def size(self):
        return len(self.queue)

    # Display queue
    def display(self):
        print(list(self.queue))


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
print("Is Empty:", q.is_empty())