import fileinput
import functools

PUZZLE = "".join(fileinput.input())
PATTERNS, TOWELS = PUZZLE.split("\n\n")
PATTERNS = sorted(PATTERNS.split(", "))
TOWELS = TOWELS.split("\n")
PART_1, PART_2 = 0, 0

@functools.lru_cache()
def num_designs(towel, patterns):
    poss = 0
    for pattern in patterns:
        l = len(pattern)
        if towel == pattern:
            poss += 1
        if towel[:l] == pattern:
            sub_poss = num_designs(towel[l:], patterns)
            if sub_poss:
                poss += sub_poss
    return poss





for towel in TOWELS:
    output = num_designs(towel, frozenset(PATTERNS))
    if output:
        PART_1 += 1
    PART_2 += output
    

print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")