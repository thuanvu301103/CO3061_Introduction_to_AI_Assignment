import random
import copy

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
                    if row_curr == row:
                        return False
                    if cross_1_curr == cross_1:
                        return False
                    if cross_2_curr == cross_2:
                        return False
                        #print ("Solution is False")
                        #return False
            #print ("Solution is True")
            return True


class dfs (n_queens): 
    def sol(self):
        stack = [self.initstate]
        self.visited = []
        while len(stack) != 0:
            curr_state = stack.pop(-1)
            #if self.check_sol(curr_state): return curr_state
            if len(curr_state) == self.n: return curr_state
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

class hillclimbing:
    def __init__ (self, n):
        self.n = n
        self.initstate = []
        for i in range(self.n):
            self.initstate += [random.randint(1, self.n)]
    def h(self, state):
        h = 0
        for i in range(1, self.n):
            row = state[i-1]
            cross_1 = row + (i-1)
            cross_2 = row + (self.n-i)
            for j in range(i+1, self.n + 1):
                row_curr = state[j-1]
                cross_1_curr = row_curr + (j-1)
                cross_2_curr = row_curr + (self.n-j)
                if row_curr == row: h += 1
                if cross_1_curr == cross_1: h += 1
                if cross_2_curr == cross_2: h += 1
        return h

    def sol(self):
        curr_state = self.initstate
        h = self.h(curr_state)
        while h != 0:
            lst = []
            for i in range(1, self.n+1):
                for j in range (1, self.n+1):
                    new_state = copy.copy(curr_state)
                    if curr_state[i-1] == j: continue
                    new_state[i-1] = j
                    new_h = self.h(new_state)
                    if new_h <= h:
                        if new_h == h: lst += [new_state]
                        if new_h < h: 
                            lst = [new_state]
                            h = new_h
            if lst == []: 
                print ("No solution, try again")
                return []
            curr_state = random.choice(lst)
        return curr_state
 

    
