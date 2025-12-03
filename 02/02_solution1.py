#!/usr/bin/python3

import re
import sys

def solve(fn):
    # not a large input for part 1, so we can keep this simple and
    # read the whole line and parse it out
    product_id_ranges = []
    with open(fn) as f:
        for line in f.readlines():
            product_id_ranges = parse_ranges(line.strip())
    print(product_id_ranges)

    total_sum_invalid = 0
    for product_id_range in product_id_ranges:
        total_sum_invalid += sum_invalid_in_range(product_id_range[0], product_id_range[1])
    print(total_sum_invalid)

def parse_ranges(s):
    r = []
    product_range_strings = s.split(',')
    for product_range_string in product_range_strings:
        r.append([(x, int(x), len(x)) for x in product_range_string.strip().split('-')])
    return r

def sum_invalid_in_range(start, end):
    return sum_invalid_in_range_regex(start, end)

def sum_invalid_in_range_regex(start, end):
    sum_invalid = 0
    (start_value_str, start_value, start_value_len) = start
    (end_value_str, end_value, end_value_len) = end

    r = re.compile(r'^([1-9][0-9]*)\1$')
    for i in range(start_value, end_value + 1):
        result = r.match(str(i))
        if result is not None:
            sum_invalid += i
    return sum_invalid

if __name__ == '__main__':
    fn = '02_input.txt' # 24043483400
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
