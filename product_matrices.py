def multiplying_matrices(matrixA, matrixB):
    rows_A, columns_A = len(matrixA), len(matrixA[0])
    rows_B, columns_B = len(matrixB), len(matrixB[0])

    # Check if multiplication is possible
    if columns_A != rows_B:
        raise ValueError("Number of columns in matrix A must match the number of rows in matrix B for multiplication.")

    # Initialize the resulting product matrix with zeros
    product_matrix = [[0] * columns_B for _ in range(rows_A)]

    # Perform the matrix multiplication
    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                # Convert elements to float (or int) to ensure numeric multiplication
                matrixA[i][k] = float(matrixA[i][k])
                matrixB[k][j] = float(matrixB[k][j])
                product_matrix[i][j] += matrixA[i][k] * matrixB[k][j]

    return product_matrix