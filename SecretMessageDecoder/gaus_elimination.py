def gaussian_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        # Partial pivoting
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Make the diagonal elements 1
        pivot = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= pivot

        # Eliminate other rows
        for j in range(n):
            if j != i:
                factor = matrix[j][i]
                for k in range(i, n):
                    matrix[j][k] -= factor * matrix[i][k]

    # Extract the solution
    solution = [row[-1] for row in matrix]

    return solution

# Example usage
matrix = [
    [122, 122, 116],
    [122, 122, 83],
    [122, 122, 57],
    [113, 74, 126],
    [113, 74, 69],
    [113, 74, 41],
]


result = gaussian_elimination(matrix)
print("Solution:", result)
