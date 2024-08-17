def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        new_matrix = []
        for j in range(m):
            new_matrix.append(value)
            matrix.append(new_matrix)
    return matrix


get_matrix = get_matrix(3, 4, 5)
print(get_matrix)
