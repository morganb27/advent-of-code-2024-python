import fileinput
from collections import defaultdict

PUZZLE = "".join(line for line in fileinput.input())
RULES, UPDATES = map(str.split, PUZZLE.split("\n\n"))
PART_1, PART_2 = 0, 0

# Parse the input
RULES_DICT = defaultdict(list)
for rule in RULES:
    left, right = rule.split("|")
    RULES_DICT[left].append(right)

UPDATES = list(line.split(',') for line in UPDATES)
UNORDERED = []

# Solve problem

# Part 1
for update in UPDATES:
    for i, page in enumerate(update):
        if not all(next_page in RULES_DICT[page] for next_page in update[i+1:]):
            UNORDERED.append(update)
            break
    else:
        middle = len(update)//2
        PART_1 += int(update[middle])


# Part 2
for unordered_update in UNORDERED:
    n = len(unordered_update)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unordered_update[j] in RULES_DICT[unordered_update[j + 1]]:
                unordered_update[j], unordered_update[j + 1] = unordered_update[j + 1], unordered_update[j]
    middle = len(unordered_update)//2
    PART_2 += int(unordered_update[middle])
    
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")
    
                


