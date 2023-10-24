# -*- coding: utf-8 -*-

import random
import numpy as np
import copy
from treelib import Node, Tree
import ast
import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm, ListedColormap


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
        print (states)
        print ("Number of visited states: " + str(len(states)))
    tree = Tree()
    for i in range(len(states)):
        if len(states[i]) == 0:
            tree.create_node("start", f"{i}")
        else:
            parent = i
            while (len(states[parent])+1 != len(states[i])):
                parent = parent - 1
            if len(states[i]) == n:
                tree.create_node("final", f"{i}", f"{parent}")
            else:
                tree.create_node(f"[{i}]", f"{i}", f"{parent}" )  
    tree.save2file ('tree.txt')
    print ("Enter <end> to stop traver tree.")
    a = input("Traver node: ")
    while a != "end":
        visual(n, states[int(a)])
        a = input("Traver node: ")


class n_queens:
    def __init__(self, n):
        # Number of queens 
        self.n = n
        # Initial state
        self.initstate = []

    def add_queen (self, curr_state, x):
        new_state = curr_state + [x]
        if len(curr_state) == 0: return new_state
        for col in range(1, len(new_state)):
            row = curr_state[col-1]
            if x == row or abs(x-row) == abs(len(new_state)-col):
                return []
        return new_state

    def add_state(self, file, state):
        file.write("[")
        if len(state) != 0:
            file.write(str(state[0]))
            file.writelines([', ' + str(val) for val in state[1:]])
        file.write("]\n")


class dfs (n_queens): 
    def solve (self):
        visited = open("visitedtree.txt", "w")
        #self.initstate = []
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
                            print (h)
            
            if lst == []: 
                print ("No solution, try again")
                return []
            curr_state = random.choice(lst)
        return curr_state
    def sol_1(self):
        curr_state = self.initstate
        h = self.h(curr_state)
        while h != 0:
            lst = []
            col = random.randint(1, self.n)
            for i in range(1, self.n+1):
                new_state = copy.copy(curr_state)
                if curr_state[col-1] == i: continue
                new_state[col-1] = i
                new_h = self.h(new_state)
                print (h)
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
 

    
