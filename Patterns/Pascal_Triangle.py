n = int(input("Enter number of rows: "))

for i in range(n):

    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=" ")

    value = 1

    # Print Pascal numbers
    for j in range(i + 1):
        print(value, end="   ")
        value = value * (i - j) // (j + 1)

    print()

# ranges are very important if it differ it will make the big difference
