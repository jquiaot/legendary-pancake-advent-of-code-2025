#!/usr/bin/python3

import bisect
import sys

def solve(fn: str) -> None:
    ranges = []
    ingredients = []
    with open(fn) as f:
        parsing_ranges = True
        for line in f.readlines():
            line = line.strip()
            if line == '':
                parsing_ranges = False
                continue
            if parsing_ranges:
                parts = line.split('-')
                ranges.append((int(parts[0]), int(parts[1])))
            else:
                ingredients.append(int(line))
    print(ranges)
    print(ingredients)

    consolidated_ranges = consolidate_ranges(ranges)
    print(consolidated_ranges)

    # (range_map, range_start_list) = map_ranges(consolidated_ranges)
    # print(range_map)

    total_possible_fresh_ingredients = count_all_possible_fresh_ingredients(consolidated_ranges)
    print(total_possible_fresh_ingredients)

def consolidate_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_ranges = sorted(ranges, key = lambda x: x[0])
    consolidated_ranges = []

    cur_range = None
    for range in sorted_ranges:
        if cur_range is None:
            cur_range = (range[0], range[1])
        else:
            if cur_range[1] + 1 >= range[0]:
                cur_range = (cur_range[0], max(cur_range[1], range[1]))
            else:
                consolidated_ranges.append(cur_range)
                cur_range = (range[0], range[1])
    if cur_range is not None:
        consolidated_ranges.append(cur_range)
    return consolidated_ranges

def map_ranges(sorted_consolidated_ranges: list[tuple[int, int]]) -> dict[int, tuple[int, int]]:
    range_map = {}
    range_start_list = []
    for range in sorted_consolidated_ranges:
        range_map[range[0]] = range
        range_start_list.append(range[0])
    return (range_map, range_start_list)

def is_in_range(range_map, range_start_list: list[int], ingredient: int) -> bool:
    elt = bisect.bisect(range_start_list, ingredient)
    if elt > 0:
        range_start = range_start_list[elt - 1]
        range = range_map[range_start]
        # print(f"ingredient={ingredient} range={range}")
        return range[0] <= ingredient and ingredient <= range[1]
    return False

def count_all_possible_fresh_ingredients(consolidated_ranges: list[tuple[int, int]]) -> int:
    total_possible = 0
    for range in consolidated_ranges:
        total_possible += (range[1] - range[0]) + 1
    return total_possible

if __name__ == '__main__':
    fn = '05_input.txt' # 359913027576322
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
