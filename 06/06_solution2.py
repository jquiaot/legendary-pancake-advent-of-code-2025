#!/usr/bin/python3

from math import prod
import sys

def solve(fn):
    # we have to read lines raw
    matrix = []
    ops = []
    with open(fn) as f:
        for line in f.readlines():
            line = line.rstrip()
            if line[0] in { '*', '+' }:
                ops = line
            else:
                matrix.append(line)

    # for line in matrix:
    #     print(line)
    # print(ops)

    # test_matrix(matrix, ops)

    new_matrix = rotate_matrix(matrix)
    discrete_ops = ops.split()

    rotated_numbers = [(''.join(row)).strip() for row in new_matrix]

    # start walking from 0..len(new_matrix), when we encounter
    # a completely blank line, we pull an op from the back of
    # discrete_ops and apply it to the numbers

    total = 0
    op_index = len(discrete_ops) - 1
    cur_collected_numbers = []
    for i in range(len(rotated_numbers)):
        if rotated_numbers[i] == '':
            op_fn = None
            if discrete_ops[op_index] == '*':
                op_fn = lambda l: prod(l)
            else:
                op_fn = lambda l: sum(l)
            subtotal = op_fn(cur_collected_numbers)
            total += subtotal
            op_index -= 1
            cur_collected_numbers = []
            # print(f"op={discrete_ops[op_index]}, numbers={cur_collected_numbers}, subtotal={subtotal}")
        else:
            cur_collected_numbers.append(int(rotated_numbers[i]))

    if len(cur_collected_numbers) > 0:
        op_fn = None
        if ops[op_index] == '*':
            op_fn = lambda l: prod(l)
        else:
            op_fn = lambda l: sum(l)
        total += op_fn(cur_collected_numbers)
    print(total)

def test_matrix(matrix: list[list[int]], ops: list[int]) -> None:
    # indices of the ops dictates where a problem starts (and where the next one starts)
    for x in range(len(ops)):
        if ops[x] in { '*', '+' } and x > 0:
            # test if all of column (x-1) is blank
            all_blank = True
            a = x - 1
            for y in range(len(matrix)):
                if matrix[y][a] != ' ':
                    all_blank = False
                    break
            print(f"Column {a} all blank? {all_blank}")

# Rotates the matrix 90 degrees counterclockwise
#
# Example:
#
# 123 328  51 64
#  45 64  387 23
#   6 98  215 314
#
# =>
#
#   4
# 431
# 623
# 
# 175
# 581
#  32
# 
# 8
# 248
# 369
# 
# 356
# 24
# 1

def rotate_matrix(matrix: list[str]) -> list[list[int]]:
    # pad short lines
    longest_line_len = 0
    for line in matrix:
        longest_line_len = max(longest_line_len, len(line))
    for i in range(len(matrix)):
        matrix[i] = matrix[i] + ' ' * (longest_line_len - len(matrix[i]))

    rotated = []
    for y in range(longest_line_len - 1, -1, -1):
        rotated.append([matrix[x][y] for x in range(len(matrix))])
    # print(rotated)

    # for row in rotated:
    #     print(''.join(row))

    return rotated

if __name__ == '__main__':
    fn = '06_input.txt' # 10442199710797
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
