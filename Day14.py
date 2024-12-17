import fileinput
from collections import Counter
from utils import mul

PUZZLE = [line.strip() for line in fileinput.input()]
ROBOTS = []
RANGE = 100
PUZZLE_WIDTH = 101
PUZZLE_HEIGHT = 103
QUANDRANT = Counter()

# Parse the input
for line in PUZZLE:
    left, right = line.split()
    px, py = map(int, left.strip("p=").split(","))
    vx, vy = map(int, right.strip("v=").split(","))
    ROBOTS.append((px, py, vx, vy))

# Solve problem
# Part 1
for _ in range(1, RANGE + 1):
    new_robots = []
    for robot in ROBOTS:
        px, py, vx, vy = robot
        px = (px + vx) % PUZZLE_WIDTH
        py = (py + vy) % PUZZLE_HEIGHT
        new_robots.append((px, py, vx, vy))
    ROBOTS = new_robots

for px, py, _, _ in ROBOTS:
    if px < PUZZLE_WIDTH // 2 and py < PUZZLE_HEIGHT // 2:
        QUANDRANT[1] += 1
    if px > PUZZLE_WIDTH // 2 and py < PUZZLE_HEIGHT // 2:
        QUANDRANT[2] += 1
    if px < PUZZLE_WIDTH // 2 and py > PUZZLE_HEIGHT // 2:
        QUANDRANT[3] += 1
    if px > PUZZLE_WIDTH // 2 and py > PUZZLE_HEIGHT // 2:
        QUANDRANT[4] += 1

PART_1 = mul(QUANDRANT.values())

print(f"Solution to part 1 is: {PART_1}")

