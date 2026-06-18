graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(node, goal, limit, path):
    path.append(node)

    if node == goal:
        return True

    if limit == 0:
        path.pop()
        return False

    for neighbor in graph[node]:
        if dls(neighbor, goal, limit - 1, path):
            return True

    path.pop()
    return False

def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        path = []

        print(f"\nSearching at Depth Limit = {depth}")

        if dls(start, goal, depth, path):
            print("Goal Found!")
            print("Path:", " -> ".join(path))
            return

    print("Goal Not Found")

start = 'A'
goal = 'F'
max_depth = 5

ids(start, goal, max_depth)