import fileinput
from collections import defaultdict

PUZZLE = "".join(line for line in fileinput.input())
RULES, UPDATES = map(str.split, PUZZLE.split("\n\n"))
PART_1 = 0

# Parse the input
RULES_DICT = defaultdict(list)
for rule in RULES:
    left, right = rule.split("|")
    RULES_DICT[left].append(right)

UPDATES = list(line.split(',') for line in UPDATES)

# Solve problem

# Part 1
VALID = []
for update in UPDATES:
    for i, page in enumerate(update):
        if not all(next_page in RULES_DICT[page] for next_page in update[i+1:]):
            break
    else:
        middle = len(update)//2
        PART_1 += int(update[middle])
    
print(f"Solution to part 1 is: {PART_1}")
    
                


