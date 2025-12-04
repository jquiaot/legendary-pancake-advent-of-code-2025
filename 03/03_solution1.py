#!/usr/bin/python3

import sys

def solve(fn):
    banks = []
    with open(fn) as f:
        for line in f.readlines():
            if line.strip() == '':
                continue
            banks.append([int(x) for x in line.strip()])
    # print(banks)
    total_joltage = 0
    for bank in banks:
        total_joltage += make_joltage(bank)
    print(total_joltage)
    
def make_joltage(bank):
    on_batteries = [bank[-2], bank[-1]]
    for i in range(len(bank) - 3, -1, -1):
        if bank[i] >= on_batteries[0]:
            if on_batteries[0] > on_batteries[1]:
                on_batteries[1] = on_batteries[0]
            on_batteries[0] = bank[i]
    return on_batteries[0] * 10 + on_batteries[1]

if __name__ == '__main__':
    fn = '03_input.txt' # 17244
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
