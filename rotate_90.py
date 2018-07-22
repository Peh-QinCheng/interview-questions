def rotate(matrix):
    n = len(matrix)
    new_mat = [ [] for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_mat[j].insert(0,matrix[i][j])
    return new_mat