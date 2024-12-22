import fileinput
from utils import Point
from utils import DIRS_4
import heapq

PUZZLE = [line.strip() for line in fileinput.input()]
BOARD = {}
PART_1 = 0

# Parse the input
for y in range(len(PUZZLE)):
    for x in range(len(PUZZLE[0])):
        p = Point(x, y)
        if PUZZLE[y][x] == "S":
            START = p
            BOARD[p] = "."
        elif PUZZLE[y][x] == "E":
            END = p
            BOARD[p] = "."
        elif PUZZLE[y][x] == "#":
            BOARD[p] = "#"
        elif PUZZLE[y][x] == ".":
            BOARD[p] = "."

print("END COORD", END)
# Solve problem
# Part 1
PRIORITY_QUEUE = [(0, START, DIRS_4[1])]
VISITED_COSTS = {}
SEATS = set()

while PRIORITY_QUEUE:
    current_cost, current_position, current_direction = heapq.heappop(PRIORITY_QUEUE)
    if current_position == END:
        for state in VISITED_COSTS.keys():
            SEATS.add(state[0])
        print(len(SEATS))

    if VISITED_COSTS.get((current_position, current_direction), float('inf')) <= current_cost:
        continue

    VISITED_COSTS[(current_position, current_direction)] = current_cost

    # Move forward
    neighbor_position = current_position + current_direction
    if neighbor_position in BOARD and BOARD[neighbor_position] != '#':
        heapq.heappush(PRIORITY_QUEUE, (current_cost + 1, neighbor_position, current_direction))

    # Rotate clockwise
    next_direction = DIRS_4[(DIRS_4.index(current_direction) + 1) % 4]
    heapq.heappush(PRIORITY_QUEUE, (current_cost + 1000, current_position, next_direction))

    # Rotate counterclockwise
    prev_direction = DIRS_4[(DIRS_4.index(current_direction) - 1) % 4]
    heapq.heappush(PRIORITY_QUEUE, (current_cost + 1000, current_position, prev_direction))

print(len(SEATS))