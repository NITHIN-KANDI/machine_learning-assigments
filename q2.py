def matrix_multiply(matrix_A, matrix_B):
    # Get the number of rows and columns of matrices A and B
    rows_A, cols_A = len(matrix_A), len(matrix_A[0])
    rows_B, cols_B = len(matrix_B), len(matrix_B[0]) 
    
    # Check if matrices are multiplicatable
    if cols_A != rows_B:
        return "Error: Matrices are not multiplicatable."
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)] 
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result

if __name__ == "__main__":
    # Example matrices
    matrix_A = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    matrix_B = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    # Call the matrix_multiply function
    result = matrix_multiply(matrix_A, matrix_B)   
    
    # Check the result and print accordingly
    if isinstance(result, str):
        print(result)
    else:
        print("Matrix A:")
        for row in matrix_A:
            print(row)

        print("\nMatrix B:")
        for row in matrix_B:
            print(row)

        print("\nProduct of A and B:")
        for row in result:
            print(row)
