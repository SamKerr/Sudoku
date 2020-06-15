from solver_class import Solver
from printer_utils import pretty_print, get_grid_from_filepath

class Sudoku:
    def __init__(self, filepath):
        self.model = get_grid_from_filepath(filepath)
        self.controller = Solver(self.model)

    def play_with_solver(self):
        self.controller.solve()

