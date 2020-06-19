from solver_class import Solver
from printer_utils import pretty_print, get_grid_from_filepath
import pygame as pg
import threading as thr

class Sudoku:
    def __init__(self, filepath):
        self.model = get_grid_from_filepath(filepath)
        self.controller = Solver(self.model)
    
    def event_loop(self):
        while True:
            event = pg.event.wait()
            if event.type == pg.QUIT:
                raise SystemExit

    def play_with_solver(self):    
        # create solver and have it run as Daemon (exits when main thread exits)
        solver = thr.Thread(target=self.controller.solve, args=())
        solver.setDaemon(True)
        solver.start()

        self.event_loop()