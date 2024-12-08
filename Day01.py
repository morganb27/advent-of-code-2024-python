import fileinput
from collections import Counter

PUZZLE = [line.strip() for line in fileinput.input()]
LEFT_LIST, RIGHT_LIST = [], []
PART_1, PART_2 = 0, 0

# Parse input.
for line in PUZZLE:
    left, right = line.split()
    LEFT_LIST.append(left)
    RIGHT_LIST.append(right)
LEFT_LIST = sorted(map(int, LEFT_LIST))
RIGHT_LIST = sorted(map(int, RIGHT_LIST))
RIGHT_LIST_COUNTER = Counter(RIGHT_LIST)

# Solve problem.
for left, right in zip(LEFT_LIST, RIGHT_LIST):
    delta = abs(left - right)
    PART_1 += delta
    PART_2 += left * RIGHT_LIST_COUNTER[left]

print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")








