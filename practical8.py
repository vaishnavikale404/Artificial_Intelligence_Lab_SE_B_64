# Example graph with costs between nodes
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}

# Heuristic values (estimate cost from node to goal)
heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def a_star(start, goal):
    open_list = set([start])      # Nodes to explore
    closed_list = set()           # Explored nodes
    g = {start: 0}                # Cost from start to node
    parents = {start: None}       # To rebuild path

    while open_list:
        # Pick node with lowest f(n) = g(n) + h(n)
        current = min(open_list, key=lambda node: g[node] + heuristics[node])

        # If goal found, rebuild and return path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            path.reverse()
            return path, g[goal]

        open_list.remove(current)
        closed_list.add(current)

        # Check neighbors
        for neighbor, cost in graph[current].items():
            if neighbor in closed_list:
                continue

            tentative_g = g[current] + cost

            # If neighbor not visited or found a cheaper path
            if neighbor not in open_list or tentative_g < g.get(neighbor, float('inf')):
                g[neighbor] = tentative_g
                parents[neighbor] = current
                open_list.add(neighbor)

    return None, float('inf')  # No path found

# Run the algorithm
start_node = 'S'
goal_node = 'G'
path, cost = a_star(start_node, goal_node)

if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Cost: {cost}")
else:
    print("No path found")

