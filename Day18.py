import fileinput
from utils import Point, DIRS_4
import heapq

PUZZLE = [tuple(map(int, line.strip().split(","))) for line in fileinput.input()]
BOARD = {}
START = Point(0, 0)
END = Point(70, 70)
HEIGHT = 70
WIDTH = 70
PART_1, PART_2 = None, None

def simulate(puzzle):
    # Parse the input
    for y in range(HEIGHT + 1):
        for x in range(WIDTH + 1):
            p = Point(x, y)
            if (x, y) in puzzle:
                BOARD[p] = "#"
            else:
                BOARD[p] = '.'
    # Solve problem
    PRIORITY_QUEUE = [(0, START, DIRS_4[1])]
    VISISTED_COSTS = {}

    while PRIORITY_QUEUE:
        current_cost, current_position, current_direction = heapq.heappop(PRIORITY_QUEUE)
        if current_position == END:
            print("END", current_cost, current_position, current_direction)
            PART_1 = current_cost
            return True

        if VISISTED_COSTS.get((current_position, current_direction), float("inf")) <= current_cost:
            continue

        VISISTED_COSTS[(current_position, current_direction)] = current_cost

        # Move forward
        next_position = current_position + current_direction
        if next_position in BOARD and BOARD[next_position] != "#":
            heapq.heappush(PRIORITY_QUEUE, (current_cost + 1, next_position, current_direction))
    
        # Rotate clockwise
        clockwise_rotation = DIRS_4[(DIRS_4.index(current_direction) + 1) % 4]
        heapq.heappush(PRIORITY_QUEUE, (current_cost, current_position, clockwise_rotation))

        # Rotate counterclockwise
        counterclockwise_rotation = DIRS_4[(DIRS_4.index(current_direction) + 1) % 4]
        heapq.heappush(PRIORITY_QUEUE, (current_cost, current_position, counterclockwise_rotation))
    print("last bit", puzzle[-1])
    return False


# Part 1
simulate(PUZZLE[:1024])

for i in range(1024, len(PUZZLE)):
    if not simulate(PUZZLE[:i+1]):
        PART_2 = PUZZLE[:i][-1]

print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")




    
