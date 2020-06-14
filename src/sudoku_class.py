from solver_class import Solver
from printer_utils import pretty_print, get_grid_from_filepath

class Sudoku:

    def refresh(self):
        pass 

    def solve(self, filepath):
        start = get_grid_from_filepath(filepath)
        answer = Solver().solve(start)
        if(answer is None):
            print("No solution is possible :(")
        else:
            print(pretty_print(answer))
