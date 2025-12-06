#!/usr/bin/python3

import sys

def solve(fn):
    # naive solution - read the whole dang thing into a matrix and then
    # do the math
    matrix = []
    ops = []
    with open(fn) as f:
        for line in f.readlines():
            line = line.strip()
            if line[0] in { '*', '+' }:
                ops = line.split()
            else:
                matrix.append([int(x) for x in line.split()])

    # print(matrix)
    # print(ops)
    # print(len(matrix[0]))
    # print(len(matrix))

    total = 0
    for x in range(len(matrix[0])):
        op_fn = None
        if ops[x] == '*':
            op_fn = lambda a, b: a * b
        else:
            op_fn = lambda a, b: a + b

        subtotal = matrix[0][x]
        for i in range(1, len(matrix)):
            subtotal = op_fn(subtotal, matrix[i][x])
        total += subtotal
    print(total)

if __name__ == '__main__':
    fn = '06_input.txt' # 6169101504608
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
