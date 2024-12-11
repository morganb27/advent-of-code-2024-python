import fileinput
import itertools

PUZZLE = [line.strip() for line in fileinput.input()]

PART_1 = 0

# Solve problem
# Part 1
for line in PUZZLE:
    ops = ["+", "*"]
    left, right = line.split(": ")
    left = int(left)
    nums = list(map(int, right.split()))
    for operators in itertools.product(ops, repeat=(len(nums) - 1)):
        result = int(nums[0])
        for a, b in zip(nums[1:], operators):
            if b == "+":
                result += a
            elif b == "*":
                result *= a
        if result == left:
            PART_1 += result
            break

            
print(f"Solution to part 1 is: {PART_1}")