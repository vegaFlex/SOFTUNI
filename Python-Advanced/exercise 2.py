size_matrix = int(input())
matrix = [[int(j) for j in input().split()] for i in range(size_matrix)]
# sum_diagonal = sum(matrix[i][i] for i in range(size_matrix))
# print(sum_diagonal)


# sum_diagonal = 0
# for i in range(size_matrix):
#     sum_diagonal += matrix[i][i]
# print(sum_diagonal)


# sum_diagonal = sum(matrix[size_matrix - i - 1][size_matrix - i - 1] for i in range(size_matrix))
# print(sum_diagonal)

# !!!!! - Tuk gi wyrti naobratno ot index - 1
sum_diagonal = 0
for i in range(size_matrix):
    a = matrix[size_matrix - i - 1]
    b = matrix[size_matrix - i - 1][size_matrix - i - 1]
    sum_diagonal += b
    # sum_diagonal += sum(matrix[size_matrix - i - 1][size_matrix - i - 1] for i in range(size_matrix))

