# -*- coding: utf-8 -*-
"""
@author: pc

There are various ways one could represent the state, provided that all of
the necessary information is present: where the boat is, and where the
jailers and convicts are.  For this example solution, the state is
represented by a tuple of five elements (jl,cl,b, jr,cr).
b is 'l' or 'r', representing the side of the  river where the
boat is (I don't use enumerate as the variable explorer does not display them)
The other items are the numbers of jailers and  convicts on the left and right
hand sides.
"""

"""
safe(state):
    check if a state is safe, i.e. jailers are not overpowered by convicts
    on either side of the river.
    
Note that on each side the number of convicts can exceed the number of jailers 
....when there are actually no jailers there!


"""


def safe(state):
    jl, cl, boat_position, jr, cr = state
    return (jl == 0 or jl >= cl) and (jr == 0 or jr >= cr)


"""

move(state):
    generator that returns all states that are reached from
    state, state, in one move and are safe.

There are five possible moves from left to right: move one or two jailers,
one or two convicts, or one of each.  For each of these, there is one yield.

We could make five more yield like the above for moves from right to left,
but we can instead take advantage of the symmetry of the problem.
    
"""


def move(state):
    jl, cl, boat_position, jr, cr = state
    if boat_position == 'l':
        if cl > 1:  # two convicts move
            next_state = jl, cl - 2, 'r', jr, cr + 2
            if safe(next_state):
                yield next_state
        if cl > 0:  # one convict moves
            next_state = jl, cl - 1, 'r', jr, cr + 1
            if safe(next_state):
                yield next_state
        if jl > 1:  # two jailers move
            next_state = jl - 2, cl, 'r', jr + 2, cr
            if safe(next_state):
                yield next_state
        if jl > 0:  # one jailer moves
            next_state = jl - 1, cl, 'r', jr + 1, cr
            if safe(next_state):
                yield next_state
        if jl > 0 and cl > 0:  # one convict and one jailer move
            next_state = jl - 1, cl - 1, 'r', jr + 1, cr + 1
            if safe(next_state):
                yield next_state
    else:
        # use the problem symmetry
        mirror_state = jr, cr, 'l', jl, cl
        for nextMirrorState in move(mirror_state):
            jrm, crm, boat, jlm, clm = nextMirrorState
            next_state = jlm, clm, 'l', jrm, crm
            yield next_state


"""

The goal is reached when all have crossed the river and are on the right bank
The assumption is that the initial state of the problem is when they are
all on the left bank.

Note that the is_goal function is independent of the number of jailers and 
number of convicts in the problem instance  

"""


def is_goal(state):
    jl, cl = state[0:2]
    return jl == 0 and cl == 0


"""

utilities functions to print a solution

"""


def print_state(state):
    jl, cl, boat_position, jr, cr = state
    print(jl, cl, end='')
    if boat_position == 'l':
        print(" L ", end='')
    else:
        print(" R ", end='')
    print(jr, cr, " -- ", end='')


def trans(state, state1):
    jl, cl, boat_position, jr, cr = state
    jl1, cl1, boat_position1, jr1, cr1 = state1
    if boat_position == 'l':
        if cl1 == cl - 2:
            print("2 convicts take to the the boat and row across")
        elif jl1 == jl - 2:
            print("2 jailers take to the the boat and row across")
        elif cl1 == cl:
            print("1 jailer rows across")
        elif jl1 == jl:
            print("1 convict rows across")
        else:
            print("1 convict and 1 jailer row across")
    else:
        if cr1 == cr - 2:
            print("2 convicts take to the the boat and row across")
        elif jr1 == jr - 2:
            print("2 jailers take to the the boat and row across")
        elif cr1 == cr:
            print("1 jailer rows across")
        elif jr1 == jr:
            print("1 convict rows across")
        else:
            print("1 convict and 1 jailer row across")


def print_path(path):
    print_state(path[0])
    for i in range(1, len(path)):
        trans(path[i - 1], path[i])
        print_state(path[i])


"""
dfs_rec(path):
    RECURSIVE depth first search where the list, @path, is the path  constructed so far.
    
    returns a path to the goal. "None" is used as a returned value when the search did not find
    a path to the goal

"""


# TODO EXERCISE 1
# PLEASE HAVE A LOOK AT YOUR LECTURE NOTES (THE CODE IS GIVEN IN THE LECTURE NOTES)

def dfs_stack(state):
    visited, stack = set(), [state]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(get_path([vertex] - visited, state))
    return visited

    # NON RECURSIVE version of the depth first search of a cyclic search space.
    # uses a stack of states and a dictionary @predecessor to store the predecessor of each state along the
    # search path.

    # @state: state from which the search starts
    # calls @get_path
    # calls @is_goal

    # returns a path to the goal state

    # Note: the dictionary is initialized by the statement:  predecessor = {state : None}. "None" is a marker
    # to identify the starting state when reconstruction a path by @get_path


# TODO EXERCISE 2

"""

def get_path(state,predecessor):
    Given a path specified by  @predecessor dictionary, and a @state
    returns the list of states along the path that goes from the state whose predecessor is None to @state     

"""

# TODO EXERCISE 2 utility

"""

Test of DFS recursive

print("TEST OF DFS REC:\n")
path = dfs_rec([(3, 3, 'l', 0, 0)])
print_path(path)
print("\n")
"""

"""
Test of DFS with a stack

"""

# TODO EXERCISE 2 testing

"""

dfs_path_rec(path):
    simmilar to dfs_rec but coded as a generator to return all solutions to 
    the problem. Notice the use of "yield from"

"""

# TODO Exercise 3 part recursive version

"""

dfs_path_stack(path):
    Non recursive version to find all paths to goal
    This uses a stack of paths.
    
    Using a dictionary of predecessors would not work.
    Do you figure out why?    

"""

# TODO EXERCISE 3 non-recursive version

print("TEST OF ALL SOLUTIONS DFS PATH REC:\n")

# TODO EXERCISE 3 test recursive

print("TEST OF ALL SOLUTIONS DFS STACK REC:\n")

# TODO Exercise 3 test mon-recursive

""""

Test various instances

"""
print("TESTING VARIOUS INSTANCES\n")

# TODO EXERCISE 4
