#!/usr/bin/python3

import sys

def solve(fn):
    with open(fn) as f:
        for line in f.readlines():
            pass


if __name__ == '__main__':
    fn = 'input1.txt'
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
