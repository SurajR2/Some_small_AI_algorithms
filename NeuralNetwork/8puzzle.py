import heapq
# Manhattan distance heuristic
def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != -99:
                value = state[i][j]
                goal_i, goal_j = divmod(goal_state.index(value) if value in goal_state else 0, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# A* algorithm
def astar(initial_state, goal_state):
    priority_queue = [(manhattan_distance(initial_state, goal_state), 0, initial_state)]
    heapq.heapify(priority_queue)
    visited = set()

    while priority_queue:
        _, cost, current_state = heapq.heappop(priority_queue)

        print("Step:", cost)
        for row in current_state:
            print(row)
        print()

        if current_state == goal_state:
            return current_state

        if tuple(map(tuple, current_state)) in visited:
            continue

        visited.add(tuple(map(tuple, current_state)))

        for i in range(3):
            for j in range(3):
                if current_state[i][j] == -99:
                    for d in 'UDLR':
                        next_state = [row[:] for row in current_state]

                        if d == 'U' and i > 0:
                            next_state[i][j], next_state[i - 1][j] = next_state[i - 1][j], next_state[i][j]
                        elif d == 'D' and i < 2:
                            next_state[i][j], next_state[i + 1][j] = next_state[i + 1][j], next_state[i][j]
                        elif d == 'L' and j > 0:
                            next_state[i][j], next_state[i][j - 1] = next_state[i][j - 1], next_state[i][j]
                        elif d == 'R' and j < 2:
                            next_state[i][j], next_state[i][j + 1] = next_state[i][j + 1], next_state[i][j]

                        if tuple(map(tuple, next_state)) not in visited:
                            priority = cost + 1 + manhattan_distance(next_state, goal_state)
                            heapq.heappush(priority_queue, (priority, cost + 1, next_state))


# Initial and goal states
initial_state = [[1, 2, 3], [5, 6, -99], [4, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, -99]]

# Run A* algorithm
solution_state = astar(initial_state, goal_state)
