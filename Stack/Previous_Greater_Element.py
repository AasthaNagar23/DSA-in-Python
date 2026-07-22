def previous_greater(arr):
    stack = []
    result = []

    for num in arr:

        # Remove smaller or equal elements
        while stack and stack[-1] <= num:
            stack.pop()

        # Find answer
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        # Push current element
        stack.append(num)

    return result


arr = [4, 5, 2, 25]
print(previous_greater(arr))