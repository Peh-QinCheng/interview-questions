def mat_zero(matrix):
    markers = []
    rows = []
    cols = []
    row_len = len(matrix[0])
    col_height = len(matrix)
    for i in range(col_height):
        for j in range(row_len):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    rows = list(set(rows))
    cols = list(set(cols))
    return set_zero(matrix, rows, cols)


def set_zero(matrix, rows, cols):
    row_len = len(matrix[0])
    col_height = len(matrix)
    for i in rows:
        row = matrix[i]
        for n in range(row_len):
            row[n] = 0
    for j in cols:
        for k in range(col_height):
            matrix[k][j] = 0
    return matrix

