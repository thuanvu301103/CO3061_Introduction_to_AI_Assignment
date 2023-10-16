import random

class n_queens:
    def __init__(self, n):
        # Number of queens 
        self.n = n
        # Initial state
        self.initstate = []

    # Add a new queen to the table at
    def place_queen (self, state, x):
        state += [x]
        row_curr = x
        cross_1_curr = row_curr + (len(state)-1)
        cross_2_curr = row_curr + (self.n-j)
        for i in range(1, len(state) + 1):
            row = state[i-1]
            cross_1 = row + (i-1)
            cross_2 = row + (self.n-i)
            for j in range(i+1, self.n + 1):
                row_curr = self.queen[j-1]
                if row_curr == None: continue
                cross_1_curr = row_curr + (j-1)
                cross_2_curr = row_curr + (self.n-j)
                if row_curr == row or cross_1_curr == cross_1 or cross_2_curr == cross_2:
                    return True
        return False

    # Check whether there are a pair of queens that attacking each other  
    # Used when add a new queen
    def conflict (self):
        '''      123
               1[***]
               2[***]
               3[***]
        '''
        for i in range(1, self.n + 1):
            row = self.queen[i-1]
            if row == None: return False
            cross_1 = row + (i-1)
            cross_2 = row + (self.n-i)
            for j in range(i+1, self.n + 1):
                row_curr = self.queen[j-1]
                if row_curr == None: continue
                cross_1_curr = row_curr + (j-1)
                cross_2_curr = row_curr + (self.n-j)
                if row_curr == row or cross_1_curr == cross_1 or cross_2_curr == cross_2:
                    return True
        return False
    
    # Check solution
    def check_sol (self, state):
        if any(x is None for x in state):
            #print ("Solution is not completed")
            return False
        else:
            for i in range(1, self.n + 1):
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


class dfs (n_queens_sol): 
    def sol(self):
        stack = [self.queen]
        visited = []
        while len(stack) != 0:
            curr_state = stack.pop(-1)
            if self.check_sol(curr_state): return curr_state
            val = random.shuffle([i for i in range(1, self.n+1)])
            for i in val:
                
            visited += [curr_state]
        #if self.check_sol(curr_state): return curr_state
        print ("No solution")
        return []



class brfs (n_queens_sol):
   pass

class heuristic:
    pass

