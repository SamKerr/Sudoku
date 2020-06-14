from solver_class import Solver
from printer_utils import pretty_print, get_grid_from_filepath

class Sudoku:
    def __init__(self, filepath):
        self.model = get_grid_from_filepath(filepath)
        self.controller = Solver(self.model)

    def play_with_solver(self):
        answer = self.controller.solve(self.model)
        if(answer is None):
            print("No solution is possible :(")
        else:
            print(pretty_print(answer))
