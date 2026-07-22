def next_greater(arr):
    stack = []
    result = []

    # Traverse from right to left
    for num in reversed(arr):   # 25,2,5,4

        # Remove smaller elements
        while stack and stack[-1] <= num:    #jab takk stak empty nahi he 
            stack.pop()

        # Find answer
        if not stack:      #jab stack empty ho then 
            result.append(-1)
        else:
            result.append(stack[-1])

        # Push current element
        stack.append(num)

    # Reverse because we processed from right to left
    return result[::-1]


arr = [4, 5, 2, 25]
print(next_greater(arr))