# Starting state
import itertools
import time
import iddfs


def part_1():
    start_states = [
        # 19 Moves
        # 2.77s
        [0, 0, [[0, 7, 1], [4, 3, 2], [8, 6, 5]]],

        # 23 moves
        # 27.20s
        [0, 2, [[5, 6, 0], [1, 3, 8], [4, 7, 2]]],

        #
        [2, 0, [[3, 5, 6], [1, 2, 7], [0, 8, 4]]],
        [1, 1, [[7, 3, 5], [4, 0, 2], [8, 1, 6]]],
        [2, 0, [[6, 4, 8], [7, 1, 3], [0, 2, 5]]],
    ]
    goal_state = [0, 2, [[3, 2, 0], [6, 1, 8], [4, 7, 5]]]
    times = []
    sol_length = []
    # Path = list of states[state, state]

    for state in start_states:
        iddfs.goal_state = goal_state

        start = time.time()

        for depth_limit in itertools.count():
            solution = iddfs.dfs_rec([state], depth_limit)
            if solution is not None:
                sol_length.append(len(solution))
                print("Number of moves : " + str(len(solution)))
                break

        finish = time.time()

        total_time = finish - start

        print("Time taken : " + str(total_time))

        times.append(total_time)

    print(times)


if __name__ == '__main__':
    part_1()
