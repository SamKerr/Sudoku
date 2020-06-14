from copy import copy, deepcopy
from gui_class import Gui

class Solver:
    """
    Solves a 9x9 sudoku grid using a heuristic based backtracking algorithm
    """

    def __init__(self, grid):
        self.model = grid
        self.view = Gui(grid)


    def get_possibilities(self, grid, i, j):
        # generate set of numbers [1,9]
        # Remove any digits that are in the same row, column or sector
        poss = set(range(1,10))
        # remove row elements
        for k in grid[i]:
            if(k in poss):
                poss.remove(k)
        
        # remove column elements
        for x in range(9):
            k = grid[x][j]
            if(k in poss):
                poss.remove(k)

        # remove sector elements
        x,y = map(lambda x: 3*(x//3), (i,j))
        for dx in range(3):
            for dy in range(3):
                k = grid[x+dx][y+dy] 
                if(k in poss):
                    poss.remove(k)
        return poss

    # TODO shouldnt require grid on first call
    def solve(self, grid):
        # Heuristic based backtracking 
        # Heursitic: Try the grid cell with the least number of possiblities first 
        # Try each possibility for the cell, calling on solve recursively until either
        #           (i) a grid cell with 0 possibilities is found, on which we backtrack and try the next possibility
        #           (ii) A grid with no empty cells is found

        # Note: minPos has 10 elements which is larger than any number of possibilities in 9x9 sudoku
        isComplete = True
        minPos, minCoords = set(range(10)), (None,None) 
        for i in range(9):
            for j in range(9):
                if(grid[i][j] is None):
                    isComplete = False
                    poss = self.get_possibilities(grid,i,j)
                    if(len(poss) < len(minPos)):
                        minPos = poss
                        minCoords = (i,j)        
        
        if(isComplete):
            return grid
        else: 
            i,j = minCoords
            poss = minPos
            result = None 
            while(result == None):
                if(len(poss) == 0):
                    return None
                else:
                    candiate = poss.pop()
                    grid[i][j] = candiate
                    self.view.update_square(i,j,candiate)
                    gridArgument = deepcopy(grid)
                    result = self.solve(gridArgument)
            return result