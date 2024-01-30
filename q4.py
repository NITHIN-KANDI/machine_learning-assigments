def transpose_matrix(matrix):
    transposed_matrix=[]

    for col in range(len(matrix[0])):
        transposed_row = [matrix[row][col] for row in range(len(matrix))]
        transposed_matrix.append(transposed_row)

    return transposed_matrix


if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Call the transpose_matrix function and print the result
    print("Original Matrix:")
    for row in matrix:
        print(row)

    print("\nTransposed Matrix:")
    result = transpose_matrix(matrix)
    for row in result:
        print(row)
