import random
import numpy as np

class n_queens:
    def __init__(self, n):
        # Number of queens 
        self.n = n
        # Initial state
        self.initstate = np.array([], dtype = np.int64)
        # Backtracking
        #self.visited = []

    # Add a new queen to the table at
    def place_queen (self, state, x):
        '''      123
               1[***]
               2[***]
               3[***]
        ''' 
        if len(state) == 0: new_state = np.append([],np.array([x, x+len(state), x+self.n-len(state)-1]))
        else: new_state = np.append(state, np.array([x, x+len(state), x+self.n-len(state)-1]))
        print(new_state)
        if len(new_state) == 1: return new_state
        #row_curr = x
        #cross_1_curr = row_curr + (len(new_state)-1)
        #cross_2_curr = row_curr + (self.n-len(new_state))
        for i in range(1, len(new_state)):
            row = new_state[i-1]
            cross_1 = row + (i-1)
            cross_2 = row + (self.n-i)
            #if row_curr == row or cross_1_curr == cross_1 or cross_2_curr == cross_2:
            if new_state[-1][0] == row or cross_1 == new_state[-1][1] or cross_2 == new_state[-1][2]:
                    return np.array([], dtype = np.int64)
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
        #stack = np.array([self.initstate])
        #print ("Stack: ", stack)
        #self.visited = []
        while len(stack) != 0:
            curr_state = stack.pop(-1)
            #curr_state = stack[-1]
            #stack = stack [:-1]
            #print ("Stack + len: ", stack, len(stack))
            #print ("Curent state: ", curr_state)
            if self.check_sol(curr_state): return curr_state
            val = [i for i in range(1, self.n+1)] 
            random.shuffle(val)
            #print(val)
            for i in val:
                #print (i)
                new_state = self.place_queen(curr_state, i)
                if len(new_state) == 0: continue
                stack += [new_state]
                #stack = np.append(stack, new_state)
            #self.visited += [curr_state]
        #if self.check_sol(curr_state): return curr_state
        print ("No solution")
        return []



class brfs (n_queens):
   pass

class heuristic:
    pass
