# -*- coding: utf-8 -*-
"""
@author: pc

Solution to the jailers and convicts problem.

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
    jl, cl, boatPosition, jr, cr = state
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
    jl, cl, boatPosition, jr, cr = state
    if (boatPosition == 'l'):
        if cl > 1:  # two convicts move
            nextState = jl, cl - 2, 'r', jr, cr + 2
            if safe(nextState):
                yield nextState
        if cl > 0:  # one convict moves
            nextState = jl, cl - 1, 'r', jr, cr + 1
            if safe(nextState):
                yield nextState
        if jl > 1:  # two jailers move
            nextState = jl - 2, cl, 'r', jr + 2, cr
            if safe(nextState):
                yield nextState
        if jl > 0:  # one jailer moves
            nextState = jl - 1, cl, 'r', jr + 1, cr
            if safe(nextState):
                yield nextState
        if jl > 0 and cl > 0:  # one convict and one jailer move
            nextState = jl - 1, cl - 1, 'r', jr + 1, cr + 1
            if safe(nextState):
                yield nextState
    else:
        # use the problem symmetry
        mirrorState = jr, cr, 'l', jl, cl
        for nextMirrorState in move(mirrorState):
            jrm, crm, boat, jlm, clm = nextMirrorState
            nextState = jlm, clm, 'l', jrm, crm
            yield nextState


"""

The goal is reached when all have crossed the river and are on the right bank
The assumption is that the initial state of the problem is when they are
all on the left bank.

Note that the is_goal function is independent of the number of jailers and 
number of convicts in the problem instance  

"""


def is_goal(state):
    jl, cl = state[0:2]
    return (jl == 0 and cl == 0)


"""

utilities

"""


def print_state(state):
    jl, cl, boatPosition, jr, cr = state
    print(jl, cl, end='')
    if (boatPosition == 'l'):
        print(" L ", end='')
    else:
        print(" R ", end='')
    print(jr, cr, " -- ", end='')


def trans(state, state1):
    jl, cl, boatPosition, jr, cr = state
    jl1, cl1, boatPosition1, jr1, cr1 = state1
    if boatPosition == 'l':
        if cl1 == cl - 2:
            print("2 convicts take to the the boat and row accross")
        elif jl1 == jl - 2:
            print("2 jailers take to the the boat and row accross")
        elif cl1 == cl:
            print("1 jailer rows accross")
        elif jl1 == jl:
            print("1 convict rows accross")
        else:
            print("1 convict and 1 jailer row accros")
    else:
        if cr1 == cr - 2:
            print("2 convicts take to the the boat and row accross")
        elif jr1 == jr - 2:
            print("2 jailers take to the the boat and row accross")
        elif cr1 == cr:
            print("1 jailer rows accross")
        elif jr1 == jr:
            print("1 convict rows accross")
        else:
            print("1 convict and 1 jailer row accros")


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


def dfs_rec(path):
    if is_goal(path[-1]):
        return path
    else:
        for nextState in move(path[-1]):
            if nextState not in path:
                nextPath = path + [nextState]
                solution = dfs_rec(nextPath)
                if solution != None:
                    return solution
    return None


"""

dfs_stack(state):
    NON RECURSIVE version of the depth first search of a cyclic search space.
    uses a stack of states, @state, and a dictionary @predecessor to store the predecessor of each state along the 
    search path.
    
    @state: state from which the search starts
    calls @get_path 
    calls @is_goal
    
    returns a path to the goal state 
    
    Note: the dictionary is initialized by the statement:  predecessor = {state : None}. "None" is a marker 
    to identify the starting state when reconstruction a path by @get_path

"""


def dfs_stack(state):
    predecessor = {state: None}
    stack = [state]
    while stack != []:
        state = stack.pop()
        path = get_path(state, predecessor)
        if is_goal(state):
            return path
        else:
            for nextState in move(state):
                if nextState not in path:
                    stack.append(nextState)
                    predecessor[nextState] = state
    return None


"""

def get_path(state,predecessor):
    Given a path specified by  @predecessor dictionary, and a @state
    returns the list of spaces along the path that goes from the state whose predecessor is None to @state     

"""


def get_path(state, predecessor):
    path = []
    while (state != None):
        path = [state] + path
        state = predecessor[state]
    return path


"""

Test of DFS recursive

"""
print("TEST OF DFS REC:\n")
path = dfs_rec([(3, 3, 'l', 0, 0)])
print_path(path)
print("\n")
"""

Test of DFS with a stack

"""
print("TEST OF DFS STACK:\n")
path = dfs_stack((3, 3, 'l', 0, 0))
print_path(path)
print("\n")

"""

dfs_path_rec(path):
    simmilar to dfs_rec but coded as a generator to return all solutions to 
    the problem. Notice the use of "yield from"

"""


def dfs_path_rec(path):
    if is_goal(path[-1]):
        yield path
    else:
        for nextState in move(path[-1]):
            if nextState not in path:
                nextPath = path + [nextState]
                yield from dfs_path_rec(nextPath)


"""

dfs_path_stack(path):
    Non recursive version to find all paths to goal
    This uses a stack of paths.
    
    Using a dictionary of predecessors would not work.
    Do you figure out why?    

"""


def dfs_path_stack(path):
    stack = [path]
    while stack != []:
        path = stack.pop()
        if is_goal(path[-1]):
            yield path
        else:
            for nextState in move(path[-1]):
                if nextState not in path:
                    stack.append(path + [nextState])


print("TEST OF ALL SOLUTIONS DFS PATH REC:\n")

for path in dfs_path_rec([(3, 3, 'l', 0, 0)]):
    print_path(path)
    print("\n")

print("TEST OF ALL SOLUTIONS DFS STACK REC:\n")

for path in dfs_path_stack([(3, 3, 'l', 0, 0)]):
    print_path(path)
    print("\n")

""""

Test various instances

"""
print("TESTING VARIOUS INSTANCES\n")

list_state = [
    (2, 2, 'l', 0, 0),
    (4, 4, 'l', 0, 0),
    (5, 4, 'l', 0, 0),
]

for state in list_state:
    print("starting from", state),
    solution = dfs_rec([state])
    if (solution == None):
        print("No solution\n")
    else:
        print_path(solution)
        print("\n")
