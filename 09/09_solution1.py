#!/usr/bin/python3

import sys

def solve(fn: str) -> None:
    tiles = []
    with open(fn) as f:
        for line in f:
            line = line.strip()
            coords = line.split(',')
            tiles.append((int(coords[0]), int(coords[1])))
    #print(tiles)

    find_largest_rectangle_naive(tiles)

"""
Stupid naive solution -- just calculate pair-wise areas and see which is largest.
We probably need to sort in some way to make it more efficient.

EDIT: Never mind, it actually completed quickly.
"""
def find_largest_rectangle_naive(tiles: list[tuple[int, int]]) -> None:
    largest_area = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = abs(tiles[i][0] - tiles[j][0] + 1) * abs(tiles[i][1] - tiles[j][1] + 1)
            largest_area = max(largest_area, area)
    print(largest_area)


if __name__ == '__main__':
    fn = '09_input.txt' # 4750297200
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
