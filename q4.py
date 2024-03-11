def transpose_matrix(matrix):
    # Initialize an empty list to store the transposed matrix
    transposed_matrix = []

    # Iterate through each column of the original matrix
    for col in range(len(matrix[0])):
        # Create a transposed row by taking elements from each row in the original matrix corresponding to the current column
        transposed_row = [matrix[row][col] for row in range(len(matrix))]
        
        # Append the transposed row to the transposed matrix
        transposed_matrix.append(transposed_row)

    # Return the transposed matrix
    return transposed_matrix


if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Print the original matrix
    print("Original Matrix:")
    for row in matrix:
        print(row)

    # Call the transpose_matrix function and print the result
    print("\nTransposed Matrix:")
    result = transpose_matrix(matrix)
    for row in result:
        print(row)
