#!/usr/bin/python3

import sys

def solve(fn):
    grid = []
    with open(fn) as f:
        for line in f.readlines():
            line = line.strip()
            grid.append([x for x in line])
    # print_grid(grid)

    width = len(grid[0])
    height = len(grid)
    # print(f"width={width}, height={height}")

    num_adjacent_grid = [[0 for x in range(width)] for y in range(height)]
    # print_grid(num_adjacent_grid)

    for x in range(width):
        for y in range(height):
            if grid[y][x] == '@':
                for (a, b) in gen_coordinates(width, height, x, y):
                    num_adjacent_grid[b][a] += 1
    # print_grid(num_adjacent_grid)

    num_accessible_rolls = 0
    for x in range(width):
        for y in range(height):
            if grid[y][x] == '@' and num_adjacent_grid[y][x] < 4:
                num_accessible_rolls += 1
    print(num_accessible_rolls)

def print_grid(g):
    for row in g:
        print(row)
    

def gen_coordinates(w, h, x, y):
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            if a >= 0 and a < w and b >= 0 and b < h:
                if not (a == x and b == y):
                    yield (a, b)

if __name__ == '__main__':
    fn = '04_input.txt' # 1437
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
