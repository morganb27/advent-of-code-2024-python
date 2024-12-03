import fileinput
from itertools import pairwise

PUZZLE = [[int(x) for x in line.strip().split()] for line in fileinput.input()]
PART_1, PART_2 = 0, 0
print(PUZZLE)

# Solve problem.
for report in PUZZLE:
    # PART 1
    if all(a < b and b <= a + 3 for a, b in pairwise(report)):
        PART_1 += 1
        PART_2 += 1
    elif all(a > b and a <= b + 3 for a, b in pairwise(report)):
        PART_1 += 1
        PART_2 += 1

    #PART 2
    elif sum(all(a < b and b <= a + 3 for a, b in pairwise(report[:i] + report[i+1:])) for i in range(len(report))) >= 1:
        PART_2 += 1
    elif sum(all(a > b and a <= b + 3 for a, b in pairwise(report[:i] + report[i+1:])) for i in range(len(report))) >= 1:
        PART_2 += 1


print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")