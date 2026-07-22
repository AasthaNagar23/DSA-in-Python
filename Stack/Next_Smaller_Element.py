def next_smaller(arr):
    stack = []
    result = []

    # Traverse from right to left
    for num in reversed(arr):

        # Remove greater or equal elements
        while stack and stack[-1] >= num:
            stack.pop()

        # Find answer
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        # Push current element
        stack.append(num)

    # Reverse the result
    return result[::-1]


arr = [4, 8, 5, 2, 25]
print(next_smaller(arr))