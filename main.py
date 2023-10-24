# -*- coding: utf-8 -*-

from nqueens import *
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm, ListedColormap


def test_3():
    A = dfs(1)
    lst = A.solve()
    print(lst)
    visual(A.n, lst)
    gen_tree(A.n)

def test_4():
    A = hillclimbing(25)
    lst = A.solve()
    print(lst)
    if (lst != None):
        visual(A.n, lst)

#test_3()
test_4()
