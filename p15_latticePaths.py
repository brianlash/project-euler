# Starting in the top left corner of a 2×2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom
# right corner.
#
# (Image removed)
#
# How many such routes are there through a 20×20 grid?


# For a grid of size n x n there are (2n)!/(n!)^2 routes, ie. (40!)/(20! * 20!)
# The following code prompts the user for a grid size and enumerates all paths,
# returning the sum.

# Step 1: Make the list of node names for the 20x20 grid
# Step 2: Convert the graph to a python dictionary
# Step 3: Use DFS algorithm to enumerate all possible paths/return their count

# helper function using code under Path function at this link:
# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python

graph_size = int(input('Graph size? (Ex. ''3'' for for 3x3) ')) + 1

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Step 1:
node_names = []

for x in range(65,91):
    node_names.append(chr(x))

node_names = node_names * 20

node_names = node_names[:graph_size ** 2]

# Create a list of A's, B's, C's etc...
temp_assignment = []

for x in range(65,80):
    for y in range(26):
        temp_assignment.append(chr(x))

del temp_assignment[(graph_size ** 2) - graph_size:]

for x in range(26, graph_size ** 2):
    node_names[x] = temp_assignment.pop(0) + node_names[x]

nodes_list = []

for x in range(graph_size):
    new_row = []
    for x in range(graph_size):
        new_row.append(node_names.pop(0))
    nodes_list.append(new_row)

# Step 2:
nodes_matrix = {}

for x in range(graph_size):
    if x == graph_size - 1:
        for y in range(graph_size - 1):
            nodes_matrix[nodes_list[x][y]] = set([nodes_list[x][y+1]])
    else:
        for y in range(graph_size):
            if y == graph_size - 1:
                nodes_matrix[nodes_list[x][y]] = set([nodes_list[x+1][y]])
            else:
                nodes_matrix[nodes_list[x][y]] = set([nodes_list[x][y+1], \
                    nodes_list[x+1][y]])

# Step 3 (With assist from helper function above)
paths = list(dfs_paths(nodes_matrix, nodes_list[0][0], nodes_list[-1][-1]))

print(len(paths))
