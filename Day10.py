import fileinput
from utils import Point
from collections import defaultdict

PUZZLE = [list(line.strip()) for line in fileinput.input()]
GRAPH = defaultdict(set)
PART_1, PART_2 = 0, 0

def dfs(graph, node, visited=None, part_2=False):
    if visited is None:
        visited = []   
        
    if node[0] == '9':
        if part_2:
            visited.append(node)
        else:
            if node not in visited:
                visited.append(node)
    
    for neigh in graph.get(node, []):
        dfs(graph, neigh, visited, part_2)
    return visited


# Parse the input
for y in range(len(PUZZLE)):
    for x in range(len(PUZZLE[0])):
        if PUZZLE[y][x] != '.':
            curr = Point(x, y)
            key = (PUZZLE[y][x], curr)
            for neigh in curr.neighbours():
                nx, ny = neigh.x, neigh.y
                if 0 <= nx < len(PUZZLE[0]) and 0 <= ny < len(PUZZLE) and PUZZLE[ny][nx] != '.':
                    neigh_value = PUZZLE[ny][nx]
                    if int(neigh_value) == int(PUZZLE[y][x]) + 1:
                        GRAPH[key].add((neigh_value, Point(nx, ny)))

# Solve problem
# Part 1
for node in GRAPH:
    if node[0] == '0':
        visited = dfs(GRAPH, node)
        PART_1 += len(visited)

# Part 2
for node in GRAPH:
    if node[0] == '0':
        visited = dfs(GRAPH, node, part_2=True)
        PART_2 += len(visited)

print(f"Solution to part 1 is: {PART_1}")
print(f"Solution to part 2: {PART_2}")
            

