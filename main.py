import sys


def create_matrix(n):
    matrix = []
    lst = []
    input_lst = input("Please enter a list of numbers which separated by comma: ").split(",")
    for num in input_lst:
        if num.isnumeric():
            lst.append(float(num))
        else:
            print(f"Invalid Input!!! {num} is not a number!!!")
            sys.exit()

    if verify_matrix(n, input_lst):
        counter = 0
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(float(input_lst[counter]))
                counter += 1
            matrix.append(temp)
        print(matrix)
    return matrix


def verify_matrix(n, lst):
    if len(lst) > (n ** 2):
        print("You entered more numbers!!")
        return False
    elif len(lst) < (n ** 2):
        print("You entered many numbers!!")
        return False
    else:
        return True


def row_check(matrix, n):
    values = []
    for i in range(0, n):
        row_sum = 0
        for j in range(0, n):
            row_sum += matrix[i][j]
        values.append(row_sum)
        if values[0] != values[i]:
            return False
    return values[0]


def col_check(matrix, n):
    values = []
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += matrix[i][j]
        values.append(sum)
        if values[0] != values[j]:
            return False
    return values[0]


def main_diagonal_check(matrix, n):
    sum = 0
    for i, j in enumerate(range(n)):
        sum += matrix[i][j]
    return sum


def secondary_diagonal_check(matrix, n):
    sum = 0
    for i, j in enumerate(range(n)):
        sum += matrix[i][n - j - 1]
    return sum


def main():
    n = int(input("Please enter dim of matrix: "))
    matrix = create_matrix(n)

    if row_check(matrix, n) == col_check(matrix, n) == main_diagonal_check(matrix, n) == secondary_diagonal_check(
            matrix, n):
        print("Valid")
    else:
        print("Invalid")


main()


#  A = 16,2,3,13,5,11,10,8,9,7,6,12,4,14,15,1
#  B = 15,10,3,6,4,5,16,9,14,11,2,7,1,8,13,12

