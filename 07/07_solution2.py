#!/usr/bin/python3

import sys

def solve(fn: str) -> None:
    # current line is where the beams currently are
    cur_line = None
    # transform the first line into 0's and 1's for convenience
    start_translation_table = str.maketrans(".S", "01")

    max_len = None
    max_len_minus_two = None

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
                    # basically, when we encounter a splitter, we keep
                    # accumulating beams, and we make sure we propagate
                    # the same number of beams to left and right
                    if line[i] == '^' and cur_line[i] >= 1:
                        if i > 0:
                            cur_line[i - 1] += cur_line[i]
                        if i < max_len_minus_two:
                            cur_line[i + 1] += cur_line[i]
                        # we still zero out the beam on the current
                        # splitter index
                        cur_line[i] = 0
    print(cur_line)
    print(sum(cur_line))


if __name__ == '__main__':
    fn = '07_input.txt' # 108924003331749
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
