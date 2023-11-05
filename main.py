# -*- coding: utf-8 -*-

from nqueens import *
from support import *
import numpy as np 

def test_1():
    print ("---Test n = 1")
    A = dfs(1)
    lst = A.solve()
    print("Answer: ", lst)
    visual(A.n, lst)
    
    print ("---Test n = 2")
    B = dfs(2)
    lst = B.solve()
    visual(B.n, lst)

    print ("---Test n = 4")
    C = dfs(4)
    lst = C.solve()
    print("Answer: ", lst)
    visual(C.n, lst)
    gen_tree_dfs(C.n)
    for i in range(count_visited()):
        trav_state(C.n, i+1)

def test_2():
    print ("---Test n = 4")
    C = dfs(4)
    lst = C.solve()
    print("Answer: ", lst)
    visual(C.n, lst)

    print ("---Test n = 4")
    C = dfs(4)
    lst = C.solve()
    print("Answer: ", lst)
    visual(C.n, lst)

    print ("---Test n = 4")
    C = dfs(4)
    lst = C.solve()
    print("Answer: ", lst)
    visual(C.n, lst)
    

def test_3():
    print ("---Test n = 100")
    D = dfs(100)
    lst = D.solve()
    print("Answer: ", lst)
    visual(D.n, lst)
    if check_sol(lst):
        print ("Answer is True")
    else:  
        print ("Answer is False")

def test_4():
    print ("---Test n = 1")
    A = brfs(1)
    lst = A.solve()
    print("Answer: ", lst)
    visual(A.n, lst)
    
    print ("---Test n = 2")
    B = brfs(2)
    lst = B.solve()
    visual(B.n, lst)

    print ("---Test n = 4")
    C = brfs(4)
    lst = C.solve()
    print("Answer: ", lst)
    visual(C.n, lst)
    gen_tree_brfs(C.n)
    for i in range(count_visited()):
        trav_state(C.n, i+1)

def test_5():
    print ("---Test n = 10")
    B = brfs(10)
    lst = B.solve()
    print("Answer: ", lst)
    visual(B.n, lst)

def test_6():
    print ("---Test n = 2")
    A = hillclimbing(2)
    lst = A.solve()
    visual(A.n, lst)

    print ("---Test n = 10")
    A = hillclimbing(10)
    lst = A.solve()
    print("Answer: ", lst)
    visual(A.n, lst)

def test_7():
    print ("---Test n = 30")
    A = hillclimbing(30)
    lst = A.solve()
    print("Answer: ", lst)
    visual(A.n, lst)


def test_8():
    print ("---Test n = 30")
    A = hillclimbing(30)
    lst = A.solve_1()
    print("Answer: ", lst)
    visual(A.n, lst)


test_8()
