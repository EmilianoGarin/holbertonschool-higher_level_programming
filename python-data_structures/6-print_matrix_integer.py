#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in enumerate(matrix):
        for x in enumerate(i[1]):
            if x[0] == len(i[1]) - 1:
                print("{}".format(x[1]), end="")
            else:
                print("{} ".format(x[1]), end="")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
