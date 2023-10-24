# -*- coding: utf-8 -*-

import random
import numpy as np
import copy
from treelib import Node, Tree
import ast
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, ListedColormap
import threading


def visual(n, lst): 
    #if lst == []: 
    #    return
    dx, dy = 1, 1
    P = np.arange(-8.0, 8.0, dx) 
    Q = np.arange(-8.0, 8.0, dy)  
    min_max = np.min(P), np.max(P), np.min(Q), np.max(Q) 
    res = np.add.outer(range(n), range(n)) % 2
    for i in range(len(lst)):
        res[lst[i]-1][i] = -1
    cmap = ListedColormap(["green", "white", "lightgrey"])
    plt.imshow(res, cmap=cmap, vmin=-1, vmax=1)
    plt.xticks([]) 
    plt.yticks([]) 
    #plt.title("Using Matplotlib Python to Create chessboard") 
    plt.show()

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

    def add_queen (self, curr_state, x):
        new_state = curr_state + [x]
        if len(curr_state) == 0: return new_state
        for col in range(1, len(new_state)):
            row = curr_state[col-1]
            if x == row or abs(x-row) == abs(len(new_state)-col):
                return []
        return new_state

class dfs (blind_search): 

    def solve (self):
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
                new_state = self.add_queen(curr_state, i)
                if new_state == []: continue
                stack += [new_state] 
            #print(curr_state)
        print ("No solution")
        visited.close()
        return []

class brfs (blind_search):
   pass

class hillclimbing (n_queens):
        
    def f(self, state):
        f = 0
        for i in range(1, self.n):
            row_curr = state[i-1]
            for j in range(i+1, self.n+1):
                row = state[j-1]
                if row == row_curr: f += 1
                elif abs(row_curr-row) == abs(i-j): f += 1
        return f

    def get_neighbour(self, state):
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

    def get_neighbour_1(self, state):
        # optimal state with minumun heuristic function value
        op_state = state
        f = self.f(op_state)
        neighbour_state = copy.copy(state)
        col = random.randint(1, self.n)
        new_states = []
        for j in range (1, self.n+1):
            # condition for skipping the curent state
            if j != state[col-1]:
                neighbour_state[col-1] = j
                temp = self.f(neighbour_state)
                if temp <= f:
                    f = temp
                    op_state = copy.copy(neighbour_state)
                neighbour_state = copy.copy(state)
        return (op_state, f)

    def solve_1(self):
        #visited = open("visitedtree.txt", "w")
        self.initstate = []
        for i in range(self.n):
            self.initstate += [random.randint(1, self.n)]
        neighbour_state = self.initstate
        while True:
            # generate current state since neighbour state has become curent state
            curr_state = neighbour_state
            
            (neighbour_state, neighbour_f) = self.get_neighbour_1(curr_state)
            print(neighbour_state, neighbour_f)
            #self.add_state(visited, neighbour_state)
            if neighbour_f == 0:
                #visited.close()
                return neighbour_state
            if neighbour_state == curr_state:
                #visited.close()
                print ("No solution")
                return
            elif self.f(curr_state) == neighbour_f:
                neighbour_state = []
                for i in range(self.n):
                    neighbour_state += [random.randint(1, self.n)]      
        
    def solve(self):
        #visited = open("visitedtree.txt", "w")
        self.initstate = []
        for i in range(self.n):
            self.initstate += [random.randint(1, self.n)]
        neighbour_state = self.initstate
        init_f = self.f(self.initstate)
        count_repeat = 0
        while True:
            # generate current state since neighbour state has become curent state
            curr_state = neighbour_state
            (neighbour_state, neighbour_f) = self.get_neighbour(curr_state)
            print(neighbour_state, neighbour_f)
            #self.add_state(visited, neighbour_state)
            if neighbour_f == 0:
                #visited.close()
                return neighbour_state
            if neighbour_state == curr_state:
                #visited.close()
                print ("No solution")
                return
            elif self.f(curr_state) == neighbour_f:
                count_repeat += 1
                if (count_repeat <= self.n*0.5):
                    continue
                count_repeat = 0
                '''
                neighbour_state = []
                for i in range(self.n):
                    neighbour_state += [random.randint(1, self.n)]
                '''
                while True:
                    neighbour_state = []
                    for i in range(self.n):
                        neighbour_state += [random.randint(1, self.n)]
                    new_f = self.f(neighbour_state)
                    #print (abs(new_f-init_f), (self.n*0.25))
                    if abs(new_f-init_f) >= self.n*0.75:
                        init_f = new_f
                        break
    
