from collections import deque

# Create Stack
stack = deque()

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Peek
print("Top Element:", stack[-1])

# Pop
print("Popped:", stack.pop())

print("Stack after pop:", stack)

# Check if Empty
print("Is Empty:", len(stack) == 0)