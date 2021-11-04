def is_goal(state):
    # [y, x, [[0, 1, 2], [3, 4, 5], [6, 7, 8]]]
    if state == [2, 0, [[4, 2, 6], [7, 1, 8], [0, 5, 3]]]:
        return True
    else:
        return False


def get_path(state, predecessor):
    path = []
    while state is not None:
        path = [state] + path
        state = predecessor[state]
    return path


def dfs_path_rec(path):
    if is_goal(path[-1]):
        yield path
    else:
        for next_state in move(path[-1]):
            if next_state not in path:
                next_path = path + [next_state]
                yield from dfs_path_rec(next_path)


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
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield [i1, j1, grid]
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]


def dfs_rec(path):
    if is_goal(path[-1]):
        return path
    else:
        for next_state in move(path[-1]):
            if next_state not in path:
                print("Next state is not in path... ", path)
                next_path = path + [next_state]
                solution = dfs_rec(next_path)
                if solution is not None:
                    return solution
    return None


if __name__ == '__main__':
    # Starting state
    state = [1, 1, [[2, 1, 6], [4, 0, 8], [7, 5, 3]]]

    # Path = list of states[state, state]
    print("Result : ", dfs_rec([state]))
