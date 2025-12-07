#!/usr/bin/python3

import sys

def solve(fn: str) -> None:
    # current line is where the beams currently are
    cur_line = None
    # transform the first line into 0's and 1's for convenience
    start_translation_table = str.maketrans(".S", "01")

    max_len = None
    max_len_minus_two = None
    num_splits = 0

    with open(fn) as f:
        for line in f:
            line = line.strip()
            if max_len is None:
                max_len = len(line)
                max_len_minus_two = max_len - 1

            if cur_line is None:
                # establish the first line
                cur_line = [int(x) for x in list(line.translate(start_translation_table))]
            else:
                # check current line for splitters
                for i in range(len(line)):
                    if line[i] == '^' and cur_line[i] == 1:
                        num_splits += 1
                        if i > 0:
                            cur_line[i - 1] = 1
                        cur_line[i] = 0
                        if i < max_len_minus_two:
                            cur_line[i + 1] = 1
    # print(cur_line)
    print(num_splits)


if __name__ == '__main__':
    fn = '07_input.txt' # 1651
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
