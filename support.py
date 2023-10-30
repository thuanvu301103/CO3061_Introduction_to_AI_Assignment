import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm, ListedColormap
import numpy as np

# This function visualize the solution on the chessboard
def visual(n, lst): 
    if len(lst) == 0: return
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