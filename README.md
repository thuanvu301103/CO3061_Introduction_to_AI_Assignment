# CO3061_Introduction_to_AI_Assignment: N-queens problem
## Target
- Implement basic Search algorithms
- Solve the N-queens problem
## Introduce
The N-queens problem is a problem that requires placing N queens on an NxN chessboard so that there are no pairs of queens which threatens each other (queen threatens according to chess rules)
## Implementation
### Caution
In this assignment, we will use Python 3 to solve N-queens problem, so make sure that, you have aldready install these library: 
- ```random```: generate random number
- ```numpy```: generate states and better for search
### Depth Fist Search (DFS) approach
- State-space: All possible arrangements of a queens (0 < a < n), one per column in the leftmost a columns, with no queen attacking another.
- Actions: Add a queen to any square in the leftmost empty column such that it is not attacked by any other queen.
- Algorithms:
  1 Evaluate the initial state: No queen has been place on the chessboard
  2 Loop until a solution is found or there are no new operators left to be applied: 
    + Select and apply a operator 
    + Evaluate the new state: 
    goal → quit 
better than current state → new current state 
=> Not try all possible new states!
- Implementation (using Python):
  1. State: A state is represent by a 
  2. How to know if two queens attacking eachother?
### Breath Fít Search (BrFS) approach
- State-space: All possible arrangements of a queens (0 < a < n), one per column in the leftmost a columns, with no queen attacking another.
- Actions: Add a queen to any square in the leftmost empty column such that it is not attacked by any other queen.
- Algorithms
- Implementation (using Python):
  1. State:
  2. How to know if two queens attacking eachother?
### Heuristic approach
- State-space
