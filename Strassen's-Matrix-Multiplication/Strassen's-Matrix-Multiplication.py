def verify_input(X):
    n = len(X)
    i = 1
    while i <= n:
        if n == (2 ** i):
            return True
        i += 1
    else:
        return False


def matrix_addition(A, B):

    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result


def matrix_subtraction(A, B):

    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]
    return result


def split_matrix(matrix, row_start, row_end, col_start, col_end):

    result = []
    for i in range(row_start, row_end):
        result.append(matrix[i][col_start:col_end])
    return result


def strassen_matrix_multiply(A, B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    n = len(A)
    mid = n // 2

    # Split matrices into quadrants
    a11 = split_matrix(A, 0, mid, 0, mid)
    a12 = split_matrix(A, 0, mid, mid, n)
    a21 = split_matrix(A, mid, n, 0, mid)
    a22 = split_matrix(A, mid, n, mid, n)

    b11 = split_matrix(B, 0, mid, 0, mid)
    b12 = split_matrix(B, 0, mid, mid, n)
    b21 = split_matrix(B, mid, n, 0, mid)
    b22 = split_matrix(B, mid, n, mid, n)

    # Recursive steps
    s1 = matrix_subtraction(b12, b22)
    s2 = matrix_addition(a11, a12)
    s3 = matrix_addition(a21, a22)
    s4 = matrix_subtraction(b21, b11)
    s5 = matrix_addition(a11, a22)
    s6 = matrix_addition(b11, b22)
    s7 = matrix_subtraction(a12, a22)
    s8 = matrix_addition(b21, b22)
    s9 = matrix_subtraction(a11, a21)
    s10 = matrix_addition(b11, b12)

    # Recursive multiplications
    p1 = strassen_matrix_multiply(a11, s1)
    p2 = strassen_matrix_multiply(s2, b22)
    p3 = strassen_matrix_multiply(s3, b11)
    p4 = strassen_matrix_multiply(a22, s4)
    p5 = strassen_matrix_multiply(s5, s6)
    p6 = strassen_matrix_multiply(s7, s8)
    p7 = strassen_matrix_multiply(s9, s10)

    # Calculate result quadrants
    c11 = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    c12 = matrix_addition(p1, p2)
    c21 = matrix_addition(p3, p4)
    c22 = matrix_subtraction(matrix_subtraction(matrix_addition(p5, p1), p3), p7)

    # Combine result quadrants
    result = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            result[i][j] = c11[i][j]
            result[i][j + mid] = c12[i][j]
            result[i + mid][j] = c21[i][j]
            result[i + mid][j + mid] = c22[i][j]

    return result


def main():
    A = [[2, 5], [1, 3]]
    B = [[3, 7], [6, 6]]
    if len(A) == len(B) and verify_input(A) is True:
        result = strassen_matrix_multiply(A, B)
        for row in result:
            print(row)
    else:
        print("Invalid input!!!\nYou should enter 2^n * 2^n matrices")



main()


# Example usage
# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# B = [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]
# res = [250, 260, 270, 280] [618, 644, 670, 696] [986, 1028, 1070, 1112] [1354, 1412, 1470, 1528]

# A = [[1, 2], [5, 6]]
# B = [[5, 6], [7, 8]]
# res = [19, 22], [67, 78]

# A = [[2, 5], [1, 3]]
# B = [[3, 7], [6, 6]]
# res = [36, 44], [21, 25]

