# Results

# 18 moves
# 2.90s
# 231356 yields
# Start state : [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]
# -------------
# 22 moves
# 27.89s
# 2266209 yields
# Start state : [0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]]
# -------------
# 24 moves
# 80.80s
# 6469723 yields
# Start state : [2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]]
# -------------
# 26 moves
# 312.55s
# 25176830 yields
# Start state : [1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]]
# -------------
# 20 moves
# 7.15s
# 561396 yields
# Start state : [2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]]
# -------------


# 20 moves
# 8.78s
# 692005 yields
# Start state : [0, 0, [[0, 1, 8], [3, 6, 7], [5, 4, 2]]]
# -------------
# 14 moves
# 0.23s
# 18570 yields
# Start state : [2, 0, [[6, 4, 1], [7, 3, 2], [0, 5, 8]]]
# -------------
# 24 moves
# 61.82s
# 4737798 yields
# Start state : [0, 0, [[0, 7, 1], [5, 4, 8], [6, 2, 3]]]
# -------------
# 22 moves
# 20.18s
# 1558399 yields
# Start state : [0, 2, [[5, 4, 0], [2, 3, 1], [8, 7, 6]]]
# -------------
# 20 moves
# 7.15s
# 561396 yields
# Start state : [2, 1, [[8, 6, 7], [2, 5, 4], [3, 0, 1]]]
# -------------

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

    # if i + 1 >


def move(state):
    global yield_count
    [i, j, grid] = state
    n = len(grid)
    for pos in move_blank(i, j, n):
        i1, j1 = pos
        grid = copy.deepcopy(grid)
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield_count += 1
        yield [i1, j1, grid]
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]


def dfs_rec(path, depth):
    global yield_count
    if is_goal(path[-1]):
        return path

    if depth == 0:
        return None
    else:
        for next_state in move(path[-1]):
            if next_state not in path:
                next_path = path + [next_state]
                solution = dfs_rec(next_path, depth - 1)
                if solution is not None:
                    if yield_count > 0:
                        print("Yield count : " + str(yield_count))
                    yield_count = 0
                    return solution

    return None


if __name__ == '__main__':
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
    # Path = list of states[state, state]

    for state in start_states:
        goal_state = goal_state

        start = time.time()

        for depth_limit in itertools.count():
            solution = dfs_rec([state], depth_limit)
            if solution is not None:
                sol_length.append(len(solution))
                print("Number of moves : " + str(len(solution) - 1))
                break

        finish = time.time()

        total_time = finish - start

        print("Time taken : " + str(total_time))
        print("------------")
        times.append(total_time)
