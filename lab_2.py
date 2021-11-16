import itertools
import random
import time


def id_dfs(puzzle, goal):
    def idfs(path, depth):
        # unable to search when depth is 0
        if depth == 0:
            return
        # check if goal has been reached
        if path[-1] == goal:
            return path
        # iterate through possible moves
        for move in get_moves(path[-1]):
            # run this function on unvisited nodes, decrementing depth
            if move not in path:
                next_path = idfs(path + [move], depth - 1)
                if next_path:
                    return next_path

    # runs dfs up to a limit of depth
    # depth increases until goal is found
    for depth in itertools.count():
        path = idfs([puzzle], depth)
        if path:
            return path

def move_blank(i, j, n):
    if i + 1 < n:
        yield i + 1, j
    if i - 1 >= 0:
        yield i - 1, j
    if j + 1 < n:
        yield i, j + 1
    if j - 1 >= 0:
        yield i, j - 1


def get_moves(state):
    [i, j, grid] = state
    n = len(grid)
    for pos in move_blank(i, j, n):
        i1, j1 = pos
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]
        yield [i1, j1, grid]
        grid[i][j], grid[i1][j1] = grid[i1][j1], grid[i][j]




def dfs(puzzle, goal):
    # maintain a stack of paths
    stack = []
    # push the first path into the stack
    stack.append([puzzle])
    while stack:
        # get the first path from the stack
        path = stack.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == goal:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the stack
        for adjacent in get_moves(node):
            if adjacent not in path:
                new_path = list(path)
                new_path.append(adjacent)
                stack.append(new_path)


def bfs(puzzle, goal):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([puzzle])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == goal:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in (get_moves(node)):
            if adjacent not in path:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


if __name__ == '__main__':

    start_state = [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]]
    goal_state = [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]

    reps = 25
    print('Average solution times: ')
    # Iterative depth first search
    total_time = 0
    for i in range(reps):
        t0 = time.time()
        solution = id_dfs(start_state, goal_state)
        t1 = time.time()
        total_time += t1 - t0
    total_time /= reps
    print('Puzzle solved using iterative depth first search in', total_time, 'seconds.')  # 0.20 seconds

    # Depth first search
    total_time = 0
    for i in range(reps):
        t0 = time.time()
        solution = id_dfs(start_state, goal_state)
        t1 = time.time()
        total_time += t1 - t0
    total_time /= reps
    print('Puzzle solved using depth first search in', total_time, 'seconds.')  # 0.37 seconds

    # Breadth first search
    total_time = 0
    for i in range(reps):
        t0 = time.time()
        solution = bfs(start_state, goal_state)
        t1 = time.time()
        total_time += t1 - t0
    total_time /= reps
    print('Puzzle solved using breadth depth first search in', total_time, 'seconds.')  # 0.04 seconds
