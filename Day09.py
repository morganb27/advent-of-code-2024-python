import fileinput
from collections import defaultdict

PUZZLE = (line.strip() for line in fileinput.input())
PUZZLE = next(PUZZLE)
BLOCK = []
COMPACTED_FILE_LENGTH = 0
MAP_ID = defaultdict(int)
FREE_SPACE = defaultdict(int)

def calculate_checksum(data):
    sum = 0
    for i, item in enumerate(data):
        sum += i * item
    return sum

# Parse the input
for i, item in enumerate(PUZZLE):
    if i % 2 == 0:
        id = i // 2
        BLOCK.extend([id] * int(item))
        COMPACTED_FILE_LENGTH += int(item)
        MAP_ID[id] = int(item)
    else:
        BLOCK.extend(['.'] * int(item))
        FREE_SPACE.append(int(item))

# Solve problem
# Part 1
BLOCK_ONE = BLOCK.copy()
start, end = 0, len(BLOCK) - 1
while start < end:
    while BLOCK_ONE[start] != '.':
        start += 1
    while BLOCK_ONE[end] == '.':
        end -= 1
    BLOCK_ONE[start], BLOCK_ONE[end] = BLOCK_ONE[end], BLOCK_ONE[start]
BLOCK_ONE[start], BLOCK_ONE[end] = BLOCK_ONE[end], BLOCK_ONE[start]

# Part 2
BLOCK_TWO = BLOCK.copy()
start, end = 0, len(BLOCK) - 1


PART_1 = calculate_checksum(BLOCK_ONE[:COMPACTED_FILE_LENGTH])

print(f"Solution to part 1 is: {PART_1}")