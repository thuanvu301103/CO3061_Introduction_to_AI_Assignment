import random
import copy

class n_queens:
    def __init__(self, n):
        # Number of queens 
        self.n = n
        # Initial state
        self.initstate = [{}, {}, {}]
        # Backtracking
        self.visited = []

    # Add a new queen to the table at
    def place_queen (self, state, x):
        '''      123
               1[***]
               2[***]
               3[***]
        ''' 
        len_1 = len(state[0])
        #len_2 = len(state[1])
        #len_3 = len(state[2])
        new_state = copy.deepcopy(state)
        #print(state)
        row = x
        cross_1 = x + (len(state[0]))
        cross_2 = x + self.n-len(state[0])-1
        if len_1 == 0: 
            new_state[0].update({row:len(state)+1})
            new_state[1].update({cross_1:len(state)+1})
            new_state[2].update({cross_2:len(state)+1})
            return new_state
        #print("State: ", state)
        

        #row_curr = x
        #cross_1_curr = row_curr + (len(new_state)-1)
        #cross_2_curr = row_curr + (self.n-len(new_state))
        #for i in range(1, len(new_state)):
        #    row = state[i-1]
        #    cross_1 = row + (i-1)
        #    cross_2 = row + (self.n-i)
        if row in state[0] or cross_1 in state[1] or cross_1 in state[2]:
            return [{},{},{}]
        new_state[0].update({row:len(state)+1})
        new_state[1].update({cross_1:len(state)+1})
        new_state[2].update({cross_2:len(state)+1})
        return new_state
    
    # Check solution
    def check_sol (self, state):
        if len(state[0]) < self.n:
            return False
        else:
            row = set(state[0])
            cross_1 = set(state[1])
            cross_2 = set(state[2])
            if len(row) != len(state[0]) or len(cross_1) != len(state[1]) or len(cross_2) != len(state[2]):
                return False
            return True

            '''
            for i in range(1, self.n):
                row = state[0]
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
            '''


class dfs (n_queens): 
    def sol(self):
        stack = [self.initstate]
        #print("Stack: ", stack, len(stack))
        #self.visited = []
        while len(stack) != 0:

            curr_state = stack.pop(-1)
            #print("Stack: ", stack, len(stack))
            #if self.check_sol(curr_state): return curr_state[0]
            if len(curr_state[0]) == self.n: return curr_state[0]
            val = [i for i in range(1, self.n+1)] 
            random.shuffle(val)
            #print(val)
            for i in val:
                new_state = self.place_queen(curr_state, i)
                #print(new_state)
                if len(new_state[0]) == 0: continue
                stack += [new_state]
            #self.visited += [curr_state]
        #if self.check_sol(curr_state): return curr_state
        print ("No solution")
        return []



class brfs (n_queens):
   pass

class heuristic:
    pass
