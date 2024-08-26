def adding_matrices(matrixA, matrixB):
    add_matrix = []
    for r in range(len(matrixA)):
        sum_rows = []
        for c in range(len(matrixA[0])):
            sum_rows.append(matrixA[r][c] + matrixB[r][c])
        add_matrix.append(sum_rows)
    return add_matrix