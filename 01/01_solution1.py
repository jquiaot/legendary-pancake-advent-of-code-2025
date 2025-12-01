#!/usr/bin/python3

import sys

def solve(fn):
    # input:
    # R29
    # L38
    # L3
    # R50

    # represent "R" turns as positive, "L" turns as negative

    num_zeroes = 0
    numbers = 100
    cur = 50
    moves = []
    with open(fn) as f:
        for line in f.readlines():
            line = line.strip()
            negative = line[0] == "L"
            clicks = int(line[1:])
            if negative:
                clicks = 100 - clicks
            cur = (cur + clicks) % 100
            print(f"{line} => clicks={clicks} => cur={cur}")
            if cur == 0:
                num_zeroes += 1
    print(num_zeroes)
    # 1081

if __name__ == '__main__':
    fn = '01_input.txt'
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
