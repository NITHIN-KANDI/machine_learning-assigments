def matrix_multiply(A, B):
    rows_A,cols_A=len(A),len(A[0])
    rows_B,cols_B=len(B),len(B[0]) 
    if cols_A!=rows_B:       # Check if matrices are multiplicatable
        return "Error: Matrices are not multiplicatable."
    result=[[0 for i1 in range(cols_B)] for i2 in range(rows_A)] # Initialize result matrix with zeros

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

if __name__ == "__main__":
    # Example matrices
    A = [
        [1, 2,3],
        [4, 5, 6],
    ]

    B = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]

    
    result = matrix_multiply(A, B)   # Call the matrix_multiply function
    if isinstance(result, str):# Check the result and print accordingly
        print(result)
    else:
        print("Matrix A:")
        for row in A:
            print(row)
            print(type(result))

        print("\nMatrix B:")
        for row in B:
            print(row)

        print("\nProduct of is AB:")
        for row in result:
            print(row)
