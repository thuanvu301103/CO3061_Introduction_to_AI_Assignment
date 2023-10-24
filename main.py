# -*- coding: utf-8 -*-

from nqueens import *
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm, ListedColormap

def visual(n, lst): 
    if lst == []: 
        return
    dx, dy = 1, 1
    P = np.arange(-8.0, 8.0, dx) 
    #print(P, "\n"*3) 
    Q = np.arange(-8.0, 8.0, dy) 
    #print(Q, "\n"*3) 
    #P, Q = np.meshgrid(P, Q) 
    #print(P, "\n"*3, Q) 
    min_max = np.min(P), np.max(P), np.min(Q), np.max(Q) 
    res = np.add.outer(range(n), range(n)) % 2
    #print (res)
    for i in range(n):
        res[lst[i]-1][i] = -1
    cmap = ListedColormap(["green", "white", "lightgrey"])
    #plt.imshow(res, cmap="binary_r")
    plt.imshow(res, cmap=cmap, vmin=-1, vmax=1)
    plt.xticks([]) 
    plt.yticks([]) 
    #plt.title("Using Matplotlib Python to Create chessboard") 
    plt.show() 


def test_1 ():
    A = dfs(10)
    A.check_sol()
    #A.add_queen(1,2)
    #A.add_queen(2,1)

    #print (A.queen)
    #print (A.conflict())

def test_2 ():
    A = dfs(500)
    sol=A.solve()
    print (sol)
    #print (A.visited)

#test_2()
def test_3():
    A = dfs(4)
    lst = A.solve()
    print(lst)
    visual(A.n, lst)
    gen_tree(A.n)

def test_4():
    A = hillclimbing(1000)
    lst = A.sol_1()
    #visual(A.n, lst)
    print (lst)
test_3()
