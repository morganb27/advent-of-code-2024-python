import fileinput
import itertools

PUZZLE = [line.strip() for line in fileinput.input()]

# Solve problem
# Part 1
def solve(data, part_2=False):
    sum = 0
    for line in data:
        ops = ["+", "*"]
        if part_2:
            ops.append("||")
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
                elif b == "||":
                    result = int('{}{}'.format(result, a))
            if result == left:
                sum += result
                break
    return sum

PART_1 = solve(PUZZLE)
PART_2 = solve(PUZZLE, True)
            
print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")