# AI Coursework Questions

## Question 1

### Introduction

In order to take into account the changes to the n-tile problem  specification, investigation was first directed towards the `move_blank` function as this function controls all of the permitted moves of the problem including up, down, left and right. to meet the new specification, two new rules needed to be added to the game, a rule for moving from the bottom row of the board, to the top row of the board. The second rule that needed to be added was moving the blank tile from the top row of the board to the bottom row of the board.

### Implementation

To implemenat these new rules we need to add 2 new if-statements to the `move_blank` function one that checks if the tile is at the top of the board and one that checks if the tile is at the bottom of the board. This can be done by checking if `i + 1 # Vertical Co-ordinate` is above the top of the board and if `i - 1` is below the board. If either of these conditions are `True`, then it is possible to yield the new move by either moving the tile from the bottom of the board to the top (`i + 2`) or moving the tile from the top of the board to the bottom (`i - 2`).

## Question 2

### Introduction

Changing the new specification to also include the move of cycling the rows in a circular list will also require manipulation of the `move_blank` function as well as the `move` generation function. As the new moves will be required to manipulate the entire board and not just the single blank tile. The `move_blank` function will be able to signal to the `move` function that there is a possible move that involves moving the rows in a cyclic manner as an either positive of negative signal for either up or down. This will then be interprited by the `move` function to move the rows of the grid either in an upward cyclic motion or a downwards (negative) cyclic motion. This will then yield another 2 possible movesets for the problem.

### Implementation

To signal to the `move` function that a cyclic move is possible then a positive or negative signal needs to be passed, in order to do this with the current implementation, the best method is to return the same `i, j` coordinate values to the `move` function from the `move_blank` function where there can then be a new if-statement to check if the `i, j` values are the same from the `move_blank` function and if so wether they are positive or negative. Given this information, we can then use a combination of the `insert` method along with the `pop` method to cycle the values similar to `grid.insert(0, grid.pop(-1))` to cycle in a positive direction and `grid.insert(len(grid), grid.pop(0))` for a negative cycle.

## Question 3

### Implementation

In order to create a physical version of the problem that includes the modifications specified, it would need to take the form of a cylinder with 8 individually cured tiles that would wrap around it. This would then allow the tiles to be wrapped around the cylinder so they can be moved around individually and then the rows would also be able to be shifted vertically as per the specifications.
