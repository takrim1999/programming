def Transposed(matrix):
    new_matrix = [[None] * len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


matrix = [
    [1, 2],
    [4, 5],
    [7, 8],
]
print(Transposed(matrix))
