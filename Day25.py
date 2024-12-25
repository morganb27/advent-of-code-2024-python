import fileinput

PUZZLE = "".join(fileinput.input()).split("\n\n")
LOCKS, KEYS = [], []
PART_1 = 0


def convert_into_height(part):
    height = []
    for j in range(len(part[0])):
        sum = 0
        for i in range(len(part)):
            if part[i][j] == "#":
                sum += 1
        height.append(sum)
    return height

def is_fit(lock, key):
    for l, k in zip(lock, key):
        if l + k > 5:
            return False
    return True



for part in PUZZLE:
    part = part.split("\n")
    if part[0] == "#####":
        LOCKS.append(part)
    else:
        KEYS.append(part)


for lock in LOCKS:
    height_lock = convert_into_height(lock[1:])
    for key in KEYS:
        height_key = convert_into_height(key[:-1])
        if is_fit(height_lock, height_key):
            PART_1 += 1

print(f"Soltuion to part 1 is: {PART_1}")
