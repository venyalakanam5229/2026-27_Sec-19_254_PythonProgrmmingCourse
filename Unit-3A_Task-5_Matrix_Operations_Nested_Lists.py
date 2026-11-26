matrix_a = [[11, 27], [53, 48]]
matrix_b = [[75, 64], [70, 66]]
rows = len(matrix_a)
cols = len(matrix_a[0])
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)
print("Matrix A:", matrix_a)
print("Matrix B:", matrix_b)
print("Sum:", result)
