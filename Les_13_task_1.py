import random

def matrix_print(matrix):
	for i in matrix:
		print(i)
	print()

x = int(input("Введите длину матриц: "))
y = int(input("Введите высоту матриц: "))

matrix_a = [[random.randint(1, 10) for i in range(x + 1)] for i in range(y + 1)]
matrix_b = [[random.randint(1, 10) for i in range(x + 1)] for i in range(y + 1)]

matrix_print(matrix_a)
matrix_print(matrix_b)

result_matrix = []

for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[0])):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result_matrix.append(row)

matrix_print(result_matrix)