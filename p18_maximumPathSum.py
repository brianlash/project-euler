# Project Euler problem at https://projecteuler.net/problem=18

# Helper, same as function used for p15. A Pythonic implementation of DFS.
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

triangle = [
    [75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20,4,82,47,65],
    [19,1,23,75,3,34],
    [88,2,77,73,7,63,67],
    [99,65,4,28,6,16,70,92],
    [41,41,26,56,83,40,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71,44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
    [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

alphabet = ([chr(x) for x in range(65,91)] * 5)[:120]

for x in range(len(alphabet)):
    if 26 <= x < 52:
        alphabet[x] = 'A' + alphabet[x]
    if 52 <= x < 78:
        alphabet[x] = 'B' + alphabet[x]
    if 78 <= x < 104:
        alphabet[x] = 'C' + alphabet[x]
    if 104 <= x:
        alphabet[x] = 'D' + alphabet[x]

# Make a triangle with the same dimensions as the starter triangle, but
# replace the values with labels (Ex. A, B, C... DN, DO, DP)
labeled_triangle = []

for x in range(15):
    temp_list = []
    for y in range(x + 1):
        temp_list.append(alphabet.pop(0))
    labeled_triangle.append(temp_list)

# Create a new graph object with each node and its available subnodes
# (Ex. A: 'B', 'C')
graph = {}

for x in range(len(labeled_triangle)):
    if x == len(labeled_triangle)-1:
        for y in range(len(labeled_triangle[x])):
            graph[labeled_triangle[x][y]] = set()
    else:
        for y in range(len(labeled_triangle[x])):
            graph[labeled_triangle[x][y]] = set([labeled_triangle[x+1][y], \
                labeled_triangle[x+1][y+1]])

# Make a dict using the labels (labeled_triangle) and their original values
# (triangle) as key-value pairs
labeled_triangle_with_values = {}

for x in range(len(labeled_triangle)):
    for y in range(len(labeled_triangle[x])):
        labeled_triangle_with_values[labeled_triangle[x][y]] = triangle[x][y]

# Find every path from the top (A) to each terminal node, then calculate its sum
candidate = 0

for x in labeled_triangle[14]:
    paths = list(dfs_paths(graph, 'A', x))
    for y in paths:
        temp = 0
        for z in y:
            temp += labeled_triangle_with_values[z]
        if temp > candidate:
            candidate = temp

print(candidate)
