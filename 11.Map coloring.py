def is_valid(assignment, state, color, neighbors):
    """Check if the color assignment is valid for the given state."""
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, states, colors, neighbors):
    if len(assignment) == len(states):
        return assignment

    unassigned_states = [state for state in states if state not in assignment]
    state = unassigned_states[0]

    for color in colors:
        if is_valid(assignment, state, color, neighbors):
            assignment[state] = color
            result = backtrack(assignment, states, colors, neighbors)
            if result:
                return result
            del assignment[state]

    return None

def map_coloring(states, colors, neighbors):
    assignment = {}
    return backtrack(assignment, states, colors, neighbors)

# Example usage
states = ['A', 'B', 'C', 'D', 'E']
colors = ['Red', 'Green', 'Blue']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

solution = map_coloring(states, colors, neighbors)
print(solution)
