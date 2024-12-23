import fileinput
import math

PUZZLE = [line.strip() for line in fileinput.input()]
PUZZLE = list(map(int, PUZZLE))

def process_secret_number(secret):

    # Step 1
    res = secret * 64
    secret = res ^ secret
    secret %= 16777216

    # Step 2
    res = math.floor(secret / 32)
    secret = res ^ secret
    secret %= 16777216

    # Step 3
    res = secret * 2048
    secret = res ^ secret
    secret %= 16777216

    return secret

# Solve problem
# Part 1
PART_1 = 0
for secret in PUZZLE:
    res = secret
    for _ in range(2000):
        res = process_secret_number(res)
    PART_1 += res

print(f"Solution to part 1 is: {PART_1}")