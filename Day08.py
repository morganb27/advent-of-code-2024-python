import fileinput
from collections import defaultdict
from utils import Point
import itertools

PUZZLE = [list(line.strip()) for line in fileinput.input()]
MAP = defaultdict(list)
ANTINODES = set()

# Parse the input
for y in range(len(PUZZLE)):
    for x in range(len(PUZZLE[0])):
        if PUZZLE[y][x] != ".":
            MAP[PUZZLE[y][x]].append(Point(x, y))


# Solve Part 1
for key, values in MAP.items():
    for a, b in itertools.permutations(values, 2):
            ANTINODES.add(b)
            anti_node = b + (b - a)
            while 0 <= anti_node.x < len(PUZZLE[0]) and 0 <= anti_node.y < len(PUZZLE):
                ANTINODES.add(anti_node)
                anti_node += (b - a)

PART_2 = len(ANTINODES)

print(f"Solution to part 1 is: {PART_2}")
            