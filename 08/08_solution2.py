#!/usr/bin/python3

import math
import sys

"""
Junction boxes in x,y,z coords, e.g.

162,817,812
57,618,57
906,360,560
592,479,940

"""
def solve(fn: str) -> None:
    junction_boxes = []
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            junction_boxes.append(tuple([int(x) for x in line.split(',')]))
    # print(junction_boxes)

    # is there any way around just having to calculate pair-wise distances?
    distances = [] # tuples of (distance, box1, box2)
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            distances.append(
                (
                    euclidean_distance(junction_boxes[i], junction_boxes[j]),
                    junction_boxes[i],
                    junction_boxes[j]
                    )
                )
    distances.sort(key = lambda x: x[0])

    # list of lists of boxes joined together
    # each junction box starts in its own circuit
    circuits = []
    # dictionary of box to the circuit index that it belongs to
    box_to_circuit_index = dict()

    i = 0
    for junction_box in junction_boxes:
        circuits.append([junction_box])
        box_to_circuit_index[junction_box] = i
        i += 1
    # print(circuits)

    num_circuits = len(junction_boxes)
    i = 0
    while num_circuits > 1  and i < len(distances):
        result = combine_circuits(i, circuits, box_to_circuit_index, distances[i])
        if result:
            # we combined two circuits, leaving one less circuit available
            num_circuits -= 1
        i += 1

    print(distances[i-1][1][0] * distances[i-1][2][0])
    
def euclidean_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2) + math.pow(a[2] - b[2], 2))

# Returns boolean indicating whether we combined circuits, so we can
# count the number of circuits left.
#
def combine_circuits(i, circuits, box_to_circuit_index, d) -> bool:
    a = d[1]
    b = d[2]
    a_index = box_to_circuit_index[a]
    b_index = box_to_circuit_index[b]

    dest_index = min(a_index, b_index)
    src_index = max(a_index, b_index)

    if src_index == dest_index:
        # already in same circuit, nothing to do
        return False

    # move all boxes from src index to dest index
    for box in circuits[src_index]:
        circuits[dest_index].append(box)
        box_to_circuit_index[box] = dest_index

    # clear source circuits, since they've all been moved
    circuits[src_index] = []

    # we combined circuits, so return True
    return True

if __name__ == '__main__':
    fn = '08_input.txt' # 8368033065
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    solve(fn)
