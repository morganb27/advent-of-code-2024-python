import fileinput
from utils import Point, DIRS_8

PUZZLE = [list(line.strip()) for line in fileinput.input()]
BOARD = {}
PART_1, PART_2 = 0, 0
DIRS_4 = [Point(1, 1), Point(-1, 1), Point(-1, -1), Point(1, -1)]

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

# Part 2
for point in BOARD:
     if BOARD.get(point) == 'A':
          diag_one = set([BOARD.get(point + Point(1, 1)), BOARD.get(point + Point(-1, -1))])
          diag_two = set([BOARD.get(point + Point(1, -1)), BOARD.get(point + Point(-1, 1))])
          if diag_one == diag_two == set(['M', 'S']):
            PART_2 += 1
    
    
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 1 is: {PART_2}")

    