import fileinput
from utils import Point

PUZZLE = [list(line.strip()) for line in fileinput.input()]
PART_1 = None
POSITION = None
DIR = None
OBSTACLES = set()
SEEN = set()
DIR_4 = {
    "^": lambda p : (p + Point(-1, 0), "^") if p + Point(-1, 0) not in OBSTACLES else (p, ">"),
    ">": lambda p : (p + Point(0, 1), ">") if p + Point(0, 1) not in OBSTACLES else (p, "v"),
    "v": lambda p : (p + Point(1, 0), "v") if p + Point(1, 0) not in OBSTACLES else (p, "<"),
    "<": lambda p : (p + Point(0, -1), "<") if p + Point(0, -1) not in OBSTACLES else (p, "^")
}

# Find initial position
for i in range(len(PUZZLE)):
    for j in range(len(PUZZLE[0])):
        if PUZZLE[i][j] in DIR_4:
            POSITION = Point(i, j)
            DIR = PUZZLE[i][j]
            SEEN.add(POSITION)
        elif PUZZLE[i][j] == "#":
            OBSTACLES.add(Point(i, j))


# Solve problem
# Part 1
x, y = POSITION.x, POSITION.y
while x < len(PUZZLE) and y < len(PUZZLE[0]) and x >= 0 and y >= 0:
    POSITION, DIR = DIR_4[DIR](POSITION)
    SEEN.add(POSITION)
    x, y = POSITION.x, POSITION.y


PART_1 = len(SEEN) - 1

print(f"Solution to part 1 is: {PART_1}")