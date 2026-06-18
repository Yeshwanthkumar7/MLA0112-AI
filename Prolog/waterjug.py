from collections import deque

def water_jug():
    capacity_a = 4
    capacity_b = 3
    target = 2

    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        if a == target:
            return path

        next_states = [
            (capacity_a, b),                  # Fill A
            (a, capacity_b),                  # Fill B
            (0, b),                           # Empty A
            (a, 0),                           # Empty B
            (max(0, a-(capacity_b-b)), min(capacity_b, b+a)),  # A -> B
            (min(capacity_a, a+b), max(0, b-(capacity_a-a)))   # B -> A
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

solution = water_jug()

print("Path to Goal:")
for step in solution:
    print(step)