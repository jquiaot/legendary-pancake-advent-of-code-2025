#!/usr/bin/python3

import math
import sys

"""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}

Strategy: Indicator and buttons are binary, so convert to integer
and do XOR math.
"""
def solve(fn: str) -> None:
    machines = []
    with open(fn) as f:
        for line in f:
            line = line.strip()
            parts = line.split()
            indicator_str = parts[0]
            joltage_reqs_str = parts[-1]
            schematics_str = parts[1:-1]
            # print(f"{indicator_str}, {joltage_reqs_str}, {schematics_str}")
            indicator = mk_indicator(indicator_str)
            joltage_reqs = mk_joltage_reqs(joltage_reqs_str)
            schematics = mk_schematics(schematics_str)
            # print(f"{indicator}, {joltage_reqs}, {schematics}")
            machines.append(Machine(indicator, schematics, joltage_reqs))
    # print(machines)

    total_button_presses = 0
    for m in machines:
        total_button_presses += find_min_button_presses(m)
    print(total_button_presses)

i_t = str.maketrans(".#", "01")
def mk_indicator(s: str) -> int:
    # print(s[1:-1].translate(i_t))
    return int(s[-2:0:-1].translate(i_t), 2)

def mk_joltage_reqs(s: str) -> list[int]:
    # ignored for part 1
    return [int(x) for x in s[1:-1].split(',')]

def mk_schematics(s: list[str]) -> list[int]:
    l = []
    for t in s:
        # each "schematic" represents the bits that need to be flipped
        l.append(sum([pow(2, int(x)) for x in t[1:-1].split(',')]))
    return l

def find_min_button_presses(maquina: "Machine") -> int:
    # basically depth-first search? depth == number of steps

    # indicator state -> min steps to get there
    step_map = { 0: 0 }
    # starting/intermediate indicator values to test against
    indicator_stack = [0]
    # current number of steps
    cur_steps = 0
    # print(f"INDICATOR {maquina.indicator}")
    while True:
        cur_steps += 1
        # print(f"{cur_steps} : {indicator_stack}")
        new_indicator_stack = []
        for cur_indicator in indicator_stack:
            for button in maquina.schematics:
                result = cur_indicator ^ button
                if result == maquina.indicator:
                    # our button presses got us to the indicator value,
                    # so return the current number of steps
                    return cur_steps
                if result not in step_map:
                    # we haven't seen this number of steps before, so
                    # add it to the step map, and also add it to the
                    # stack of indicators to test next round
                    step_map[result] = cur_steps
                    new_indicator_stack.append(result)
                else:
                    # we've already seen this result, so likely we've
                    # gotten to it in fewer button presses (stack depth
                    # is smaller), so we should ignore it
                    # print(f"Already seen {result}")
                    continue
        indicator_stack = new_indicator_stack
    
class Machine:
    def __init__(self,
                 indicator: int,
                 schematics: list[int],
                 joltage_reqs: list[int]) -> None:
        self.indicator = indicator
        self.schematics = schematics
        self.joltage_reqs = joltage_reqs

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Machine[indicator={self.indicator}, schematics={self.schematics}, joltage_reqs={self.joltage_reqs}"


if __name__ == '__main__':
    fn = '10_input.txt' # 409
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
