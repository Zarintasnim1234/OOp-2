def transpose_matrix(matrix):
    # Create a new matrix to store the transposed result
    transposed = []
    
    for j in range(len(matrix[0])):  # Loop through columns
        new_row = []
        for i in range(len(matrix)):  # Loop through rows
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

# Main function to take user input
if __name__ == "__main__":
    # Input dimensions of the matrix
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    # Initialize the matrix
    matrix = []
    
    # Input elements for the matrix
    print("Enter elements of the matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    # Transpose the matrix
    transposed_matrix = transpose_matrix(matrix)

    # Display the result
    print("The transposed matrix is:")
    for row in transposed_matrix:
        print(" ".join(map(str, row)))