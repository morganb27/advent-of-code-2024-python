import fileinput
from collections import Counter

STONES = Counter(map(int, fileinput.input().readline().strip().split()))
BLINK = 75

for _ in range(BLINK):
    new_stones = Counter()
    for stone, count in STONES.items():
        stone_length = len(str(stone))
        if stone == 0:
            new_stones[1] += count
        elif int(stone_length) % 2 == 0:
            left, right = str(stone)[:int(stone_length)//2], str(stone)[int(stone_length)//2:]
            new_stones[int(left)] += count
            new_stones[int(right)] += count
        else:
            new_stones[int(stone) * 2024] += count
    STONES = new_stones

print(f"Solution to part 1 or 2 is: {sum(STONES.values())}")