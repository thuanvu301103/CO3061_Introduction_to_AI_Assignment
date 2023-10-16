import random

class n_queens:
    def __init__(self, n):
        # Number of queens 
        self.n = n
        # Initial state
        self.initstate = []
        # Backtracking
        self.visited = []

    # Add a new queen to the table at
    def place_queen (self, state, x):
        '''      123
               1[***]
               2[***]
               3[***]
        ''' 
        new_state = state + [x]
        if len(state) == 0: return new_state
        row_curr = x
        cross_1_curr = row_curr + (len(new_state)-1)
        cross_2_curr = row_curr + (self.n-len(new_state))
        for i in range(1, len(new_state)):
            row = state[i-1]
            cross_1 = row + (i-1)
            cross_2 = row + (self.n-i)
            if row_curr == row or cross_1_curr == cross_1 or cross_2_curr == cross_2:
                    return []
        return new_state
    
    # Check solution
    def check_sol (self, state):
        if len(state) < self.n:
            return False
        else:
            for i in range(1, self.n):
                row = state[i-1]
                cross_1 = row + (i-1)
                cross_2 = row + (self.n-i)
                for j in range(i+1, self.n + 1):
                    row_curr = state[j-1]
                    cross_1_curr = row_curr + (j-1)
                    cross_2_curr = row_curr + (self.n-j)
                    if row_curr == row or cross_1_curr == cross_1 or cross_2_curr == cross_2:
                        #print ("Solution is False")
                        return False
            #print ("Solution is True")
            return True


class dfs (n_queens): 
    def sol(self):
        stack = [self.initstate]
        self.visited = []
        while len(stack) != 0:
            curr_state = stack.pop(-1)
            if self.check_sol(curr_state): return curr_state
            val = [i for i in range(1, self.n+1)] 
            random.shuffle(val)
            #print(val)
            for i in val:
                new_state = self.place_queen(curr_state, i)
                if new_state == []: continue
                stack += [new_state]
            self.visited += [curr_state]
        #if self.check_sol(curr_state): return curr_state
        print ("No solution")
        return []



class brfs (n_queens):
   pass

class heuristic:
    pass

