from copy import copy, deepcopy
from gui_class import Gui
import pygame as pg 

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

    def backtracking_solver(self, grid):
        # Heuristic based backtracking sudoku solver 
        # Heursitic: Try the grid cell with the least number of possiblities first 
        # Try each possibility for the cell, calling on solve recursively until either
        #           (i) a grid cell with 0 possibilities is found, on which we backtrack and try the next possibility
        #           (ii) A grid with no empty cells is found

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
            result = None 
            i,j = minCoords
            poss = minPos
            while(result == None):
                if(len(poss) == 0):
                    return None
                else:
                    # get candidate for square
                    candiate = poss.pop()
                    grid[i][j] = candiate
                    
                    # Update model
                    gridArgument = deepcopy(grid)
                    result = self.backtracking_solver(gridArgument)

                    # update GUI
                    self.view.update_square(i,j,candiate)
            return result

    def solve(self):
        answer = self.backtracking_solver(self.model)
        if answer != None: 
            self.view.puzzle_solved()
        else: 
            self.view.puzzle_failed()
        
        while True:
            event = pg.event.wait()
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_q): 
                raise SystemExit