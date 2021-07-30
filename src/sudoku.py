from solver import Solver
from printer_utils import pretty_print, get_grid_from_filepath
import pygame as pg
import threading as thr

from typing import  List, Optional, Tuple

class Sudoku:
    def __init__(self, filepath: str):
        self.model : List[List[Optional[int]]] = get_grid_from_filepath(filepath)
        self.controller : Solver = Solver(self.model)
    
    def event_loop(self):
        while True:
            event = pg.event.wait()
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT:
                raise SystemExit
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    # create solver and have it run as Daemon (exits when main thread exits)
                    solver = thr.Thread(target=self.controller.solve, args=())
                    solver.setDaemon(True)
                    solver.start()