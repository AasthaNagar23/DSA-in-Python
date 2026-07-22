def valid_parentheses(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        # Opening brackets
        if ch in "([{":
            stack.append(ch)

        # Closing brackets
        else:
            if len(stack) == 0:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0


print(valid_parentheses("{[]}"))