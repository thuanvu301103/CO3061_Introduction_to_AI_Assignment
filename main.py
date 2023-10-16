from nqueens import *

def test_1 ():
    A = dfs(10)
    A.check_sol()
    #A.add_queen(1,2)
    #A.add_queen(2,1)

    #print (A.queen)
    #print (A.conflict())

def test_2 ():
    A = dfs(4)
    sol=A.sol()
    print (sol)

test_2()
