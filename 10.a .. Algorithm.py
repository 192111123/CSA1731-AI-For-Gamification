import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while frontier:
        current_priority, current = heapq.heappop(frontier)
        
        if current == goal:
            break
        
        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    
    return path, cost_so_far[goal]

graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1, (1, 1): 1},
    (0, 2): {(0, 1): 1, (1, 2): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(0, 2): 1, (1, 1): 1, (2, 2): 1},
    (2, 0): {(1, 0): 1, (2, 1): 1},
    (2, 1): {(2, 0): 1, (1, 1): 1, (2, 2): 1},
    (2, 2): {(2, 1): 1, (1, 2): 1}
}

start = (0, 0)
goal = (2, 2)

path, cost = a_star_search(graph, start, goal)
print(f"Path: {path}")
print(f"Cost: {cost}")
