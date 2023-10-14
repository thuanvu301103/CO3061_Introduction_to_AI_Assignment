
class n_queens_sol:
    def __init__(self, n):
        # Number of queens 
        self.n = n
        # Array that show position of queens in each column. Initial value = None
        self.queen = [None]*self.n

    # Add a new queen on the table at (x,y)
    def add_queen (self, x, y):
        self.queen[x-1] = y
        if self.conflict(): 
            self.queen[x-1] = None
            return False
        else: 
            return True

    # Check whether there are a pair of queens that attacking each other  
    # Used when add a new queen
    def conflict (self):
        '''      123
               1[***]
               2[***]
               3[***]
        '''
        for i in range(1, self.n + 1):
            row = self.queen[i-1]
            if row == None: return False
            cross_1 = row + (i-1)
            cross_2 = row + (self.n-i)
            for j in range(i+1, self.n + 1):
                row_curr = self.queen[j-1]
                if row_curr == None: continue
                cross_1_curr = row_curr + (j-1)
                cross_2_curr = row_curr + (self.n-j)
                if row_curr == row or cross_1_curr == cross_1 or cross_2_curr == cross_2:
                    return True
        return False
    
    # Check solution
    def check_sol (self):
        if any(x is None for x in self.queen):
            print ("Solution is not completed")
        else:
            for i in range(1, self.n + 1):
                row = self.queen[i-1]
                cross_1 = row + (i-1)
                cross_2 = row + (self.n-i)
                for j in range(i+1, self.n + 1):
                    row_curr = self.queen[j-1]
                    cross_1_curr = row_curr + (j-1)
                    cross_2_curr = row_curr + (self.n-j)
                    if row_curr == row or cross_1_curr == cross_1 or cross_2_curr == cross_2:
                        print ("Solution is False")
                        return False
            print ("Solution is True")
            return False


class dfs (n_queens_sol): 
    def sol(self):


class brfs (n_queens_sol):
   pass

class heuristic:
    pass

