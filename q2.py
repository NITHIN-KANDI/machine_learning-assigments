def matrix_multiply(A, B):
    # Get the number of rows and columns of matrices A and B
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0]) 
    
    # Check if matrices are multiplicatable
    if cols_A != rows_B:
        return "Error: Matrices are not multiplicatable."
    
    # Initialize result matrix with zeros
    result = [[0 for i1 in range(cols_B)] for i2 in range(rows_A)] 
    
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

if __name__ == "__main__":
    # Example matrices
    A = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    B = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    # Call the matrix_multiply function
    result = matrix_multiply(A, B)   
    
    # Check the result and print accordingly
    if isinstance(result, str):
        print(result)
    else:
        print("Matrix A:")
        for row in A:
            print(row)

        print("\nMatrix B:")
        for row in B:
            print(row)

        print("\nProduct of AB:")
        for row in result:
            print(row)
