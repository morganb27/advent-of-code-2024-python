import fileinput
import re 

PUZZLE = [line.strip() for line in fileinput.input()]
MATCHES_ONE, MATCHES_TWO = [], []
PART_1, PART_2 = 0, 0
INSTRUCTIONS = ["do()", "don't()"]

# Parse the input
for line in PUZZLE:
    MATCHES_ONE.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)", line))
    MATCHES_TWO.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line))

# Solve puzzle - Part 1 
for item in MATCHES_ONE:
    _, right = item.split("(")
    num_left, num_right = map(int, right.strip(")").split(","))
    PART_1 += num_left * num_right

# Solve puzzle - Part 2
enabled = True
for i, item in enumerate(MATCHES_TWO):
    if item == INSTRUCTIONS[1]:
        enabled = False
    elif item == INSTRUCTIONS[0]:
        enabled = True
    if enabled and item not in INSTRUCTIONS:
        _, right = item.split("(")
        num_left, num_right = map(int, right.strip(")").split(","))
        PART_2 += num_left * num_right


print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")

