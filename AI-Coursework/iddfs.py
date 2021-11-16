import copy
import itertools
import time

goal_state = []

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
    [i, j, grid] = state
    n = len(grid)
    for pos in move_blank(i, j, n):
        i1, j1 = pos
        grid = copy.deepcopy(grid)
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield [i1, j1, grid]
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]


def dfs_rec(path, depth):
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
                    return solution


    return None


if __name__ == '__main__':
    # Starting state
    state = [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]

    # Path = list of states[state, state]

    start = time.time()

    for depth_limit in itertools.count():
        solution = dfs_rec([state], depth_limit)
        if solution is not None:
            break

    finish = time.time()

    total_time = finish - start

    print(total_time)
    yield_count = 0
