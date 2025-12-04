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
        total_joltage += make_bigger_joltage(bank)
    print(total_joltage)
    
def make_bigger_joltage(bank):
    on_batteries = bank[-12:]
    print(f"bank={bank}, on_batteries={on_batteries}")
    for i in range(len(bank) - 13, -1, -1):
        if bank[i] >= on_batteries[0]:
            shuffle_joltage(on_batteries, 0)
            on_batteries[0] = bank[i]
    print(f"on_batteries={on_batteries}")
    return int(''.join([str(x) for x in on_batteries]))

def shuffle_joltage(on_batteries, idx):
    if idx < len(on_batteries) - 1 and on_batteries[idx] >= on_batteries[idx + 1]:
        shuffle_joltage(on_batteries, idx + 1)
        on_batteries[idx + 1] = on_batteries[idx]

if __name__ == '__main__':
    fn = '03_input.txt' # 171435596092638
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)


