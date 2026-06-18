from collections import deque

graph = {
    0: [1],
    1: [3, 2],
    2: [],
    3: [4],
    4: [5],
    5: [7],
    7: [6],
    6: [4]
}

# BFS
def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS:", end=" ")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

bfs(0)

print("\nDFS:", end=" ")
dfs(0, set())
