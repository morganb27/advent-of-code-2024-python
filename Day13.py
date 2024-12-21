import fileinput
import math
import re
import numpy as np

PUZZLE = "".join(fileinput.input())
ANS = 0

for block in PUZZLE.split("\n\n"):
    a, b, p = block.split("\n")
    _, right_a = a.split(": ")
    _, right_b = b.split(": ")
    _, right_p = p.split(": ")
    ax, ay = map(int, re.findall(r"\d+", right_a))
    bx, by = map(int, re.findall(r"\d+", right_b))
    px, py = map(int, re.findall(r"\d+", right_p))
    dx = math.gcd(ax, bx)
    dy = math.gcd(ay, by)
    px, py = px + 10000000000000, py + 10000000000000

    if px % dx != 0 or py % dy != 0:
        continue
    else: 
        ax, bx, px = ax // dx, bx // dx, px // dx
        ay, by, py = ay // dy, by // dy, py // dy
        A = np.array([[ax, bx], [ay, by]])
        P = np.array([px, py])
        
        try:
            m_n = np.linalg.solve(A, P)
            print(m_n)
            m, n = np.rint(m_n).astype(int)

            if m * ax + n * bx == px and m * ay + n * by == py:
                ANS += 3 * m + n
        except np.linalg.LinAlgError:
            print("No solution exists (singular matrix).")

print(f"Solution is: {ANS}")
    
