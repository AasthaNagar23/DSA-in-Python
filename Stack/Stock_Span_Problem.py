def stock_span(prices):
    stack = []          # stores indices
    span = []

    for i in range(len(prices)):

        # Remove smaller or equal prices
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        # Calculate span
        if not stack:
            span.append(i + 1)
        else:
            span.append(i - stack[-1])

        # Push current index
        stack.append(i)

    return span


prices = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(prices))