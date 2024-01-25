size_mtx = int(input())
matrix = [[int(j) for j in input().split(', ')] for i in range(size_mtx)]

primary = []
secondary = []

for idx in range(size_mtx):
    a = matrix[idx][idx]
    b = matrix[idx][size_mtx-1 - idx]

    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size_mtx-1 - idx])

print(f"Primary diagonal: {', '.join([str(el) for el in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary])}. Sum: {sum(secondary)}")
