def setZeroes(matrix):

    rows = []
    cols = []

    # Zero ki position find karo
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    # Un rows ko zero karo
    for i in rows:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0

    # Un columns ko zero karo
    for j in cols:
        for i in range(len(matrix)):
            matrix[i][j] = 0

    return matrix


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(setZeroes(matrix))