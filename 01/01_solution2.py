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
    cur = 50
    with open(fn) as f:
        for line in f.readlines():
            prev = cur
            line = line.strip()
            negative = line[0] == "L"
            clicks = int(line[1:])
            num_complete_revolutions = clicks // 100
            remainder = clicks % 100

            num_zeroes += num_complete_revolutions

            if negative:
                cur -= remainder
                if cur <= 0:
                    cur += 100
                    if prev > 0: # only increment if we "cross" 0
                        num_zeroes += 1
            else:
                cur += remainder
                if cur >= 100:
                    cur -= 100
                    if prev < 100: # only increment if we "cross" 0
                        num_zeroes += 1
            print(f"{line} => revs={num_complete_revolutions}, rem={remainder} => cur={cur} => num_zeroes={num_zeroes}")
    print(num_zeroes)
    # 6689

if __name__ == '__main__':
    fn = '01_input.txt'
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
