import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, ListedColormap
import numpy as np
from treelib import Node, Tree
import ast

# This function visualize the solution on the chessboard
def visual(n, lst): 
    #if len(lst) == 0: return
    dx, dy = 1, 1
    P = np.arange(-8.0, 8.0, dx) 
    Q = np.arange(-8.0, 8.0, dy)  
    min_max = np.min(P), np.max(P), np.min(Q), np.max(Q) 
    res = np.add.outer(range(n), range(n)) % 2
    for i in range(len(lst)):
        res[int(lst[i])-1][i] = -1
    cmap = ListedColormap(["green", "white", "lightgrey"])
    plt.imshow(res, cmap=cmap, vmin=-1, vmax=1)
    plt.xticks([]) 
    plt.yticks([])  
    plt.show()

def trav_state(n, num):
    with open ("visitedstates.txt", "r") as fp:
        lines = fp.read().splitlines()
        states = []
        for i in range (len(lines)):
            state = ast.literal_eval(lines[i])
            states += [state]
        
    visual (n, states[num-1])
    return

# This function check if the answer for n-queens problem is correct or not
def check_sol (ans):
    i = 1
    n = len(ans)
    while i < n:
        j = i + 1
        curr_row = ans[i-1]
        while j < n+1:
            row = ans[j-1]
            if row == curr_row: return False
            if abs(row- curr_row) == abs (i-j): return False
            j += 1
        i += 1
    return True

# Count number of state in "visitedstate.txt"
def count_visited():
    with open ("visitedstates.txt", "r") as fp:
        lines = fp.read().splitlines()
        states = []
        for i in range (len(lines)):
            state = ast.literal_eval(lines[i])
            states += [state]
        
        return len(states)

# Generate tree for dfs and brfs
def gen_tree_dfs (n):
    with open ("visitedstates.txt", "r") as fp:
        lines = fp.read().splitlines()
        states = []
        for i in range (len(lines)):
            state = ast.literal_eval(lines[i])
            states += [state]
        
        #print ("Number of visited states: " + str(len(states)))
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
    file = open("tree.txt", "w")
    file.close()
    tree.save2file ('tree.txt', sorting=False)

def gen_tree_brfs (n):
    with open ("visitedstates.txt", "r") as fp:
        lines = fp.read().splitlines()
        states = []
        for i in range (len(lines)):
            state = ast.literal_eval(lines[i])
            states += [state]
        
        #print ("Number of visited states: " + str(len(states)))
    tree = Tree()
    for i in range(len(states)):
        if len(states[i]) == 0:
            tree.create_node("start", f"{i+1}")
        else:
            p = i-1
            parent = states[p]
            #print (parent, states[i])
            while (parent != states[i][:-1]):
                p = p - 1
                parent = states[p]
                #print (parent, states[i])
            if len(states[i]) == n:
                tree.create_node("final", f"{i+1}", f"{p+1}")
            else:
                tree.create_node(f"[{i+1}]", f"{i+1}", f"{p+1}" )  
    file = open("tree.txt", "w")
    file.close()
    tree.save2file ('tree.txt', sorting=False)