def add_matrices(matrix1, matrix2):
    
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result


if __name__ == "__main__":
    
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    
    matrix1 = []
    matrix2 = []
    
    
    print("Enter elements of the first matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix1.append(row)
    
    
    print("Enter elements of the second matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix2.append(row)
    
    
    result_matrix = add_matrices(matrix1, matrix2)
    
    
    print("The sum of the two matrices is:")
    for row in result_matrix:
        print(" ".join(map(str, row)))