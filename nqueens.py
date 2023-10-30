# -*- coding: utf-8 -*-

import random
import numpy as np
from treelib import Node, Tree
import ast


def gen_tree (n):
    with open ("visitedtree.txt", "r") as fp:
        lines = fp.read().splitlines()
        states = []
        for i in range (len(lines)):
            state = ast.literal_eval(lines[i])
            states += [state]
        #print (states)
        print ("Number of visited states: " + str(len(states)))
    tree = Tree()
    for i in range(len(states)):
        if len(states[i]) == 0:
            tree.create_node("start", f"{i+1}")
        else:
            parent = i
            while (len(states[parent])+1 != len(states[i])):
                parent = parent - 1
            if len(states[i]) == n:
                tree.create_node("final", f"{i+1}", f"{parent+1}")
            else:
                tree.create_node(f"[{i+1}]", f"{i+1}", f"{parent+1}" )  
    tree.save2file ('tree.txt', sorting=False)
    print ("Enter <end> to stop traver tree.")
    a = input("Traver node: ")
    while a != "end":
        if a == "start": a = 1
        if a == "final": a = len(states)
        visual(n, states[int(a)-1])
        a = input("Traver node: ")

class n_queens:

    def __init__(self, n):
        # Number of queens 
        self.n = n

    def add_state(self, file, state):
        file.write("[")
        if len(state) != 0:
            file.write(str(state[0]))
            file.writelines([', ' + str(val) for val in state[1:]])
        file.write("]\n")

class blind_search (n_queens):

    def add_queen_x (self, curr_state, x):
        new_state = curr_state + [x]
        if len(curr_state) == 0: return new_state
        for col in range(1, len(new_state)):
            row = curr_state[col-1]
            if x == row or abs(x-row) == abs(len(new_state)-col):
                return []
        return new_state

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

    def solve_x (self):
        visited = open("visitedtree.txt", "w")
        self.initstate = []
        stack = [self.initstate]
        while len(stack) != 0:
            curr_state = stack.pop(-1)
            self.add_state(visited, curr_state)
            if len(curr_state) == self.n:
                visited.close()
                return curr_state
            row = [i for i in range(1, self.n+1)] 
            random.shuffle(row)
            # Generate all possible successor states by applying add_queen()
            for i in row:
                new_state = self.add_queen_x(curr_state, i)
                if new_state == []: continue
                stack += [new_state] 
            print(curr_state)
        print ("No solution")
        visited.close()
        return []

    def solve (self):
        #visited = open("visitedtree.txt", "w")
        self.initstate = np.array([], dtype="i")
        stack = [self.initstate]
        while len(stack) != 0:
            curr_state = stack.pop(-1)
            print(curr_state)
            #self.add_state(visited, curr_state)
            if len(curr_state) == self.n:
                #visited.close()
                return curr_state
            row = np.arange(1,self.n+1)
            np.random.shuffle(row)
            # Generate all possible successor states by applying add_queen()
            for i in row:
                new_state = self.add_queen(curr_state, i)
                if len(curr_state) == self.n:
                    return curr_state
                if len(new_state) == 0: continue
                stack += [new_state] 
        print ("No solution")
        #visited.close()
        return []


class brfs (blind_search):

    def solve (self):
        #visited = open("visitedtree.txt", "w")
        self.initstate = np.array([], dtype="i")
        p_queue = [self.initstate]
        while len(p_queue) != 0:
            curr_state = p_queue.pop(0)
            print(curr_state)
            #self.add_state(visited, curr_state)
            if len(curr_state) == self.n:
                #visited.close()
                return curr_state
            row = np.arange(1,self.n+1)
            np.random.shuffle(row)
            # Generate all possible successor states by applying add_queen()
            for i in row:
                new_state = self.add_queen(curr_state, i)
                if len(curr_state) == self.n:
                    return curr_state
                if len(new_state) == 0: continue
                p_queue += [new_state] 
        print ("No solution")
        #visited.close()
        return []

class hillclimbing (n_queens):

    def f(self, state):
        f = 0
        i = 1
        while i < self.n: 
        #for i in range(1, self.n):
            row_curr = state[i-1]
            j = i+1
            while j < self.n+1:
            #for j in range(i+1, self.n+1):
                row = state[j-1]
                if row == row_curr: f += 1
                elif abs(row_curr-row) == abs(i-j): f += 1
                j += 1
            i +=1
        return f

    def get_neighbour_x(self, state):
        # optimal state with minumun heuristic function value
        op_state = state
        f = self.f(op_state)
        neighbour_state = copy.copy(state)
        op_state_lst = []
        for i in range(1, self.n+1):
            for j in range (1, self.n+1):
                # condition for skipping the curent state
                if j != state[i-1]:
                    neighbour_state[i-1] = j
                    temp = self.f(neighbour_state)
                    if temp <= f:
                        if temp < f:
                            op_state_lst = []
                        op_state_lst += [neighbour_state]
                        f = temp
                    neighbour_state = copy.copy(state)
        if len(op_state_lst) != 0 and len(op_state_lst) != 1:
            op_state = op_state_lst[random.randint(0, len(op_state_lst)-1)]
        if len(op_state_lst) == 1:
            op_state = op_state_lst[0]
        return (op_state, f)

    def get_neighbour(self, state):
        # optimal state with minumun heuristic function value
        op_state = state
        init_f = self.f(op_state)
        f = init_f
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
                    temp = self.f(neighbour_state)
                    if temp == 0: return (neighbour_state, 0)
                    if temp <= f:
                        if temp < f:
                            op_state_lst = []
                        op_state_lst += [neighbour_state]
                        f = temp
                    neighbour_state = np.copy(state)
                j += 1
            i+=1
        #if init_f == f: return (op_state, f)
        if len(op_state_lst) != 0 and len(op_state_lst) != 1:
            op_state = op_state_lst[random.randint(0, len(op_state_lst)-1)]
        elif len(op_state_lst) == 1:
            op_state = op_state_lst[0]
        return (op_state, f)

    def check_conflict(self, state, q):
        i = 1
        row_curr = state[q-1]
        while i < self.n+1:
            #print (i)
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
        init_f = self.f(op_state)
        f = init_f
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
                    temp = self.f(neighbour_state)
                    if temp == 0: return (neighbour_state, 0)
                    if temp <= f:
                        if temp < f:
                            op_state_lst = []
                        op_state_lst += [neighbour_state]
                        f = temp
                    neighbour_state = np.copy(state)
                j += 1
        #if init_f == f: return (op_state, f)
            if len(op_state_lst) != 0 and len(op_state_lst) != 1:
                op_state = op_state_lst[random.randint(0, len(op_state_lst)-1)]
            elif len(op_state_lst) == 1:
                op_state = op_state_lst[0]
            return (op_state, f)
        return (op_state, f)
 
                    #-------------------------------------------------
                    #Running good: grtneigh_1_1
    def solve(self):
        #visited = open("visitedtree.txt", "w")
        self.initstate = np.random.randint(1, self.n+1, size=self.n)
        neighbour_state = self.initstate
        init_f = self.f(self.initstate)
        count_repeat = 0
        while True:
            # generate current state since neighbour state has become curent state
            curr_state = neighbour_state
            (neighbour_state, neighbour_f) = self.get_neighbour(curr_state)
            print(" h = ", neighbour_f)
            #self.add_state(visited, neighbour_state)
            if neighbour_f == 0:
                #visited.close()
                return neighbour_state
            if (neighbour_state == curr_state).all():
                #visited.close()
                print ("No solution")
                return
            elif self.f(curr_state) == neighbour_f:
                count_repeat += 1
                if (count_repeat <= self.n): continue
                neighbour_state = np.random.randint(1, self.n+1, size=self.n)
            count_repeat = 0

    def solve_1(self):
        #visited = open("visitedtree.txt", "w")
        self.initstate = np.arange(1,self.n+1)
        np.random.shuffle(self.initstate)
        neighbour_state = self.initstate
        init_f = self.f(self.initstate)
        count_repeat = 0
        while True:
            # generate current state since neighbour state has become curent state
            curr_state = neighbour_state
            (neighbour_state, neighbour_f) = self.get_neighbour_1(curr_state)
            print(" h = ", neighbour_f, "count = ", count_repeat)
            #self.add_state(visited, neighbour_state)
            if neighbour_f == 0:
                #visited.close()
                return neighbour_state
            
            #if (neighbour_state == curr_state).all():
                #visited.close()
                #print ("No solution")
                #return

            elif self.f(curr_state) == neighbour_f:
                count_repeat += 1
                if (count_repeat <= self.n): continue
                neighbour_state = np.arange(1,self.n+1)
                np.random.shuffle(neighbour_state)
            count_repeat = 0