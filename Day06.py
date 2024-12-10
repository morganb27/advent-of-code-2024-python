import fileinput
from utils import Point

PUZZLE = [list(line.strip()) for line in fileinput.input()]
PART_1, PART_2 = None, 0
POSITION = None
DIR = None
OBSTACLES = set()
SEEN = set()
DIR_4 = {
    "^": lambda p, obstacles : (p + Point(-1, 0), "^") if p + Point(-1, 0) not in obstacles else (p, ">"),
    ">": lambda p, obstacles : (p + Point(0, 1), ">") if p + Point(0, 1) not in obstacles else (p, "v"),
    "v": lambda p, obstacles : (p + Point(1, 0), "v") if p + Point(1, 0) not in obstacles else (p, "<"),
    "<": lambda p, obstacles: (p + Point(0, -1), "<") if p + Point(0, -1) not in obstacles else (p, "^")
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

# Create simulate method for both parts
def simulate(puzzle, obstacles, part_2 = False):
    dir = DIR
    seen = set()
    x, y = POSITION.x, POSITION.y
    pos = POSITION
    while x < len(puzzle) and y < len(puzzle[0]) and x >= 0 and y >= 0:
        pos, dir = DIR_4[dir](pos, obstacles)
        if part_2:
            if (pos, dir) in seen:
                return False
            seen.add((pos, dir))
        else: 
            seen.add(pos)
        x, y = pos.x, pos.y
    return len(seen) - 1

# Solve Part 1
PART_1 = simulate(PUZZLE, OBSTACLES)

# Solve Part 2
for i in range(len(PUZZLE)):
    for j in range(len(PUZZLE[0])):
        obstacles_copy = OBSTACLES.copy()
        if PUZZLE[i][j] == ".":
            obstacles_copy.add(Point(i, j))
            if not simulate(PUZZLE, obstacles_copy, True):
                PART_2 += 1

print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")