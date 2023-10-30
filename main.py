# -*- coding: utf-8 -*-

from nqueens import *
from support import *
import numpy as np 

def test_2():
    A = brfs(5)
    lst = A.solve()
    print(lst)
    visual(A.n, lst)
    #gen_tree(A.n)

def test_3():
    A = dfs(500)
    lst = A.solve()
    print(lst)
    visual(A.n, lst)
    #gen_tree(A.n)



def test_4():
    A = hillclimbing(500)
    lst = A.solve_1()
    print(lst)
    print("Answaer is correct") if check_sol(lst) else print ("Answaer is incorrect")
    visual(A.n, lst)

test_4()
#test_4()
