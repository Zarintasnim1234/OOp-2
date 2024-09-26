def multiply_matrices(matrix1, matrix2):
    # Get dimensions of the matrices
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Check if multiplication is possible
    if cols1 != rows2:
        return "Error! Number of columns in the first matrix must equal number of rows in the second matrix."
    
    # Create a result matrix with appropriate dimensions
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):  # or range(rows2)
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Main function to take user input
if __name__ == "__main__":
    # Input dimensions of the first matrix
    rows1 = int(input("Enter the number of rows for the first matrix: "))
    cols1 = int(input("Enter the number of columns for the first matrix: "))
    
    # Input dimensions of the second matrix
    rows2 = int(input("Enter the number of rows for the second matrix: "))
    cols2 = int(input("Enter the number of columns for the second matrix: "))
    
    # Check if multiplication is possible
    if cols1 != rows2:
        print("Error! Number of columns in the first matrix must equal number of rows in the second matrix.")
    else:
        # Initialize matrices
        matrix1 = []
        matrix2 = []

        # Input elements for the first matrix
        print("Enter elements of the first matrix:")
        for i in range(rows1):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            matrix1.append(row)

        # Input elements for the second matrix
        print("Enter elements of the second matrix:")
        for i in range(rows2):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            matrix2.append(row)

        # Multiply the matrices
        result_matrix = multiply_matrices(matrix1, matrix2)

        # Display the result
        print("The product of the two matrices is:")
        for row in result_matrix:
            print(" ".join(map(str, row)))