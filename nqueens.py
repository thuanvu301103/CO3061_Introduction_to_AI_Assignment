# -*- coding: utf-8 -*-

import random
import numpy as np

class n_queens:

    def __init__(self, n):
        # Number of queens 
        self.n = n

    # Add state to visited states record 
    def add_state(self, file, state):
        file.write("[")
        if len(state) != 0:
            file.write(str(state[0]))
            file.writelines([', ' + str(val) for val in state[1:]])
        file.write("]\n")

class blind_search (n_queens):

    def add_queen (self, curr_state, x):
        if len (curr_state) == 0: return np.append(curr_state, x)
        col = 1
        while col <= len(curr_state):
            row = curr_state[col-1]
            if x == row: return np.array([], dtype="i")
            if abs(x-row) == abs(len(curr_state)+1-col):
                return np.array([], dtype="i")
            col += 1
        return np.append(curr_state, x)

class dfs (blind_search): 

    def solve (self):

        visited = open("visitedstates.txt", "w")
        self.initstate = np.array([], dtype="i")
        stack = [self.initstate]

        while len(stack) != 0:

            curr_state = stack.pop(-1)
            self.add_state(visited, curr_state)

            if len(curr_state) == self.n:
                visited.close()
                return curr_state

            row = np.arange(1,self.n+1)
            np.random.shuffle(row)
            # Generate all possible successor states by applying add_queen()
            for i in row:
                new_state = self.add_queen(curr_state, i)
                if len(new_state) == self.n: return new_state
                if len(new_state) == 0: continue
                stack += [new_state] 
        
        print ("No solution")
        visited.close()
        return np.array([], dtype="i")
        
class brfs (blind_search):

    def solve (self):

        visited = open("visitedstates.txt", "w")
        self.initstate = np.array([], dtype="i")
        p_queue = [self.initstate]

        while len(p_queue) != 0:

            curr_state = p_queue.pop(0)
            self.add_state(visited, curr_state)

            if len(curr_state) == self.n:
                visited.close()
                return curr_state

            row = np.arange(1,self.n+1)
            np.random.shuffle(row)
            # Generate all possible successor states by applying add_queen()
            for i in row:
                new_state = self.add_queen(curr_state, i)
                if len(new_state) == self.n: return new_state
                if len(new_state) == 0: continue
                p_queue += [new_state] 

        print ("No solution")
        visited.close()
        return []

class hillclimbing (n_queens):

    def h(self, state):
        h = 0
        i = 1
        while i < self.n: 
            row_curr = state[i-1]
            j = i+1
            while j < self.n+1:
                row = state[j-1]
                if row == row_curr: h += 1
                elif abs(row_curr-row) == abs(i-j): h += 1
                j += 1
            i +=1
        return h

    def get_neighbour(self, state):
        # optimal state with minumun heuristic function value
        op_state = state
        init_h = self.h(op_state)
        h = init_h
        neighbour_state = np.copy(state)
        op_state_lst = []
        #neighbour_state_lst = []
        i = 1
        while i < self.n+1:
            j = 1
            while j < self.n+1:
                # condition for skipping the curent state
                if j != state[i-1]:
                    neighbour_state[i-1] = j
                    temp = self.h(neighbour_state)
                    if temp == 0: return (neighbour_state, 0)
                    if temp <= h:
                        if temp < h:
                            op_state_lst = []
                        op_state_lst += [neighbour_state]
                        h = temp
                    neighbour_state = np.copy(state)
                j += 1
            i+=1
        #if init_f == f: return (op_state, f)
        if len(op_state_lst) != 0 and len(op_state_lst) != 1:
            op_state = op_state_lst[random.randint(0, len(op_state_lst)-1)]
        elif len(op_state_lst) == 1:
            op_state = op_state_lst[0]
        return (op_state, h)

    def solve(self):

        visited = open("visitedstates.txt", "w")
        visited_h = open("visited_heuristicfunc.txt", "w")
        self.initstate = np.arange(1,self.n+1)
        np.random.shuffle(self.initstate)
        init_h = self.h(self.initstate)
        if init_h == 0: return self.initstate
        count_repeat = 0
        count_local = 0
        neighbour_state = self.initstate
        
        while True:
            # generate current state since neighbour state has become curent state
            curr_state = neighbour_state
            (neighbour_state, neighbour_h) = self.get_neighbour(curr_state)
            self.add_state(visited, neighbour_state)
            visited_h.write(str(neighbour_h) + "\n")

            if neighbour_h == 0:
                visited.close()
                visited_h.close()
                return neighbour_state
            if (neighbour_state == curr_state).all():
                count_local += 1
                if count_local > self.n:
                    visited.close()
                    visited_h.close()
                    print ("No solution")
                    return np.array([], dtype="i")
                neighbour_state = np.arange(1,self.n+1)
                np.random.shuffle(neighbour_state)
            elif self.h(curr_state) == neighbour_h:
                count_repeat += 1
                if (count_repeat <= self.n): continue
                count_local += 1
                if count_local > self.n:
                    visited.close()
                    visited_h.close()
                    print ("No solution")
                    return np.array([], dtype="i")
                neighbour_state = np.arange(1,self.n+1)
                np.random.shuffle(neighbour_state)
            count_repeat = 0

    # Improvement

    def check_conflict(self, state, q):
        i = 1
        row_curr = state[q-1]
        while i < self.n+1:
            if i == q:
                i += 1
                continue
            row = state[i-1]
            if row == row_curr: return True
            if abs(i-q) == abs(row_curr-row): return True
            i += 1
        return False

    def get_neighbour_1(self, state):
        # optimal state with minumun heuristic function value
        op_state = state
        init_h = self.h(op_state)
        h = init_h
        neighbour_state = np.copy(state)
        op_state_lst = []
        #neighbour_state_lst = []
        q = np.random.randint(1, self.n+1, size=self.n)
        for i in q:
            if not(self.check_conflict(state, i)): continue
            j = 1
            while j < self.n+1:
                # condition for skipping the curent state
                if j != state[i-1]:
                    neighbour_state[i-1] = j
                    temp = self.h(neighbour_state)
                    if temp == 0: return (neighbour_state, 0)
                    if temp <= h:
                        if temp < h:
                            op_state_lst = []
                        op_state_lst += [neighbour_state]
                        h = temp
                    neighbour_state = np.copy(state)
                j += 1
        #if init_f == f: return (op_state, f)
            if len(op_state_lst) != 0 and len(op_state_lst) != 1:
                op_state = op_state_lst[random.randint(0, len(op_state_lst)-1)]
            elif len(op_state_lst) == 1:
                op_state = op_state_lst[0]
            return (op_state, h)
        return (op_state, h)
 
    def solve_1(self):
        
        visited = open("visitedstates.txt", "w")
        visited_h = open("visited_heuristicfunc.txt", "w")

        self.initstate = np.arange(1,self.n+1)
        np.random.shuffle(self.initstate)
        neighbour_state = self.initstate
        init_h = self.h(self.initstate)
        count_repeat = 0
        count_local = 0
        while True:
            # generate current state since neighbour state has become curent state
            curr_state = neighbour_state
            (neighbour_state, neighbour_h) = self.get_neighbour_1(curr_state)
            #print ("h= ", neighbour_h, neighbour_state)

            self.add_state(visited, neighbour_state)
            visited_h.write(str(neighbour_h) + "\n")

            if neighbour_h == 0:
                visited.close()
                visited_h.close()
                return neighbour_state
            
            if (neighbour_state == curr_state).all():
                count_local += 1
                if count_local > self.n:
                    visited.close()
                    visited_h.close()
                    print ("No solution")
                    return np.array([], dtype="i")
                neighbour_state = np.arange(1,self.n+1)
                np.random.shuffle(neighbour_state)
            elif self.h(curr_state) == neighbour_h:
                count_repeat += 1
                if (count_repeat <= self.n): continue
                count_local += 1
                if count_local > self.n:
                    visited.close()
                    visited_h.close()
                    print ("No solution")
                    return np.array([], dtype="i")
                neighbour_state = np.arange(1,self.n+1)
                np.random.shuffle(neighbour_state)
            count_repeat = 0