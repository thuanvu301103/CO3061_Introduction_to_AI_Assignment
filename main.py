# -*- coding: utf-8 -*-

from nqueens import *
from support import *
import numpy as np 

def test_1():
    A = brfs(4)
    lst = A.solve()
    print(lst)
    visual(A.n, lst)
    gen_tree_brfs(A.n)

def test_2():
    A = dfs(10)
    lst = A.solve()
    print(lst)
    visual(A.n, lst)
    gen_tree_dfs(A.n)
    for i in range(7):
        trav_state(A.n, i+1)

def test_3():
    A = hillclimbing(6)
    lst = A.solve()
    print(lst)
    print("Answaer is correct") if check_sol(lst) else print ("Answaer is incorrect")
    visual(A.n, lst)

def test_4():
    A = hillclimbing(50)
    lst = A.solve_1()
    print(lst)
    print("Answaer is correct") if check_sol(lst) else print ("Answaer is incorrect")
    visual(A.n, lst)

test_2()
#test_4()
