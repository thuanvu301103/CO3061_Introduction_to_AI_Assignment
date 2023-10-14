from nqueens import *

def test_1 ():
    A = dfs(100000000)
    A.check_sol()
    #A.add_queen(1,2)
    #A.add_queen(2,1)

    #print (A.queen)
    #print (A.conflict())

test_1()
