import fileinput
from utils import Point, DIRS_8

PUZZLE = [list(line.strip()) for line in fileinput.input()]
BOARD = {}
PART_1 = 0

# Parse the input
for i in range(len(PUZZLE)):
    for j in range(len(PUZZLE[0])):
        p = Point(i, j)
        BOARD[p] = PUZZLE[i][j]

# Solve problem
# Part 1
for point in BOARD:
    for dir in DIRS_8:
        if ( 
            BOARD.get(point) == 'X'
            and BOARD.get(point + dir) == 'M'
            and BOARD.get(point + dir * 2) == 'A'
            and BOARD.get(point + dir * 3) == 'S'
            ):
                PART_1 += 1

print(f"Solution to part 1 is: {PART_1}")

    