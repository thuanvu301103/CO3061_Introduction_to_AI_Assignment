# -*- coding: utf-8 -*-

from nqueens import *
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm, ListedColormap




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
    A = dfs(10)
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
