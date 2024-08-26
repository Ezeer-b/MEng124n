def transpose_matrices(matrixA, matrixB):
    row_A = len(matrixA)
    column_A = len(matrixA[0])
    row_B = len(matrixB)
    column_B = len(matrixB[0])
    transpose_A = [[0 for _ in range(row_A)] for _ in range(column_A)]
    for i in range(row_A):
        for j in range(column_A):
            transpose_A[j][i] = matrixA[i][j]

    transpose_B = [[0 for _ in range(row_B)] for _ in range(column_B)]
    for i in range(row_B):
        for j in range(column_B):
            transpose_B[j][i] = matrixB[i][j]

    return transpose_A, transpose_B