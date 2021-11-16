import copy
import itertools
import time

goal_state = []
yield_count = 0


def is_goal(state):
    # [y, x, [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]
    # Goal State
    if state == goal_state:
        return True
    else:
        return False


def move_blank(i, j, n):
    if i + 1 < n:
        yield i + 1, j
    if i - 1 >= 0:
        yield i - 1, j
    if j + 1 < n:
        yield i, j + 1
    if j - 1 >= 0:
        yield i, j - 1


def move(state):
    [i, j, grid] = state
    n = len(grid)
    for pos in move_blank(i, j, n):
        i1, j1 = pos
        grid = copy.deepcopy(grid)
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield [i1, j1, grid]
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]


def manhattan_distance(current_state, goal_state):
    total_distance = 0

    for i in range(len(goal_state[2]) * len(goal_state[2])):

        current_state_alt = []

        for row in current_state[2]:
            for tiles in row:
                current_state_alt.append(tiles)

        goal_state_alt = []

        for row in goal_state[2]:
            for tiles in row:
                goal_state_alt.append(tiles)

        if current_state_alt[i] != 0 and current_state_alt[i] != goal_state_alt[i]:
            index = goal_state_alt.index(current_state_alt[i])
            dy = (i // len(current_state[2])) - (index // len(current_state[2]))
            dx = (i % len(current_state[2])) - (index % len(current_state[2]))
            total_distance += abs(dy) + abs(dx)
    return total_distance


def dfs_rec(path, bound):
    global yield_count

    if is_goal(path[-1]):
        return path
    if manhattan_distance(path[-1], goal_state) > bound:
        return None
    else:
        for next_state in move(path[-1]):
            if next_state not in path:
                next_path = path + [next_state]
                bound = manhattan_distance(next_path[-1], goal_state)
                solution = dfs_rec(next_path, bound)
                if solution is not None:
                    if yield_count > 0:
                        print("Yield count : " + str(yield_count))
                    yield_count = 0
                    return solution
    return None


if __name__ == '__main__':
    # Starting state
    start_states = [
        [0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]],
        [2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]],
        [0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]],
        [0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]],
        [2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]],
    ]

    goal_state = [2, 2, [[1, 2, 3], [4, 5, 6], [7, 8, 0]]]
    times = []
    sol_length = []

    for state in start_states:

        start = time.time()

        bound = manhattan_distance(state, goal_state)

        solution = dfs_rec([state], bound)

        if solution is not None:
            print("Number of moves : " + str(len(solution) - 1))

        finish = time.time()

        total_time = finish - start

        print(total_time)
        print("Time taken : " + str(total_time))
        print("------------")