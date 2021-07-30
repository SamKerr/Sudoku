import pygame as pg
from typing import Tuple, List, Optional

Colour = Tuple[int, int, int]

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

def text_objects(text: str, font: str, text_colour: Colour) -> Tuple[pg.Surface, pg.Rect]:
    textSurface = font.render(text, True, text_colour)
    print(type(textSurface.get_rect()))
    return (textSurface, textSurface.get_rect())

class Gui:
    def __init__(self, model: List[List[Optional[int]]]):
        self.grid: List[List[Optional[int]]] = model
        self.g_height: int = len(model)
        self.w_height: int = len(model[0])  
        # initialise the display
        # set up pygame
        pg.init()
        self.start_game()

    def start_game(self)-> None:
        # set dimensions
        self.rect_height, self.rect_width, self.margin  = 70, 70, 1
        self.total_rect_height, self.total_rect_width   = tuple(map(lambda x: 2*self.margin+x, (self.rect_height, self.rect_width))) 
        self.winsize = self.width, self.height          = tuple(map(lambda x: x*9, (self.total_rect_width, self.total_rect_height)))

        # set up the screen and font
        self.screen = pg.display.set_mode(self.winsize, 0, 32)
        self.screen.fill(BLACK)
        self.font = pg.font.Font("resources/Roboto-Regular.ttf", 80)
        self.message_font = pg.font.Font("resources/Roboto-Regular.ttf", 100)
        pg.display.set_caption('Sudoku')

        for row in range(self.g_height):
            for col in range(self.w_height):
                val = self.grid[row][col]
                self.draw_grid_square(row,col,val)
        pg.display.flip()

    def update_square(self, row: int, col: int, val: int)-> None:
        self.grid[row][col] = val
        self.draw_grid_square(row,col,val, RED)
        pg.display.flip()

    def draw_grid_square(self, row:int, col:int, val: int, text_colour: Colour=BLACK)-> None:
        txt = ""
        if val is None:
            txt = "X"
        else:
            txt = str(val)
        rect = [(2*self.margin + self.rect_width)*col + self.margin, 
                (2*self.margin + self.rect_height)*row + self.margin, 
                self.rect_width,
                self.rect_height]
        pg.draw.rect(self.screen, WHITE, rect)
        TextSurf, TextRect = text_objects(txt, self.font, text_colour)
        TextRect.center = (rect[0] + self.total_rect_width/2, rect[1] + self.total_rect_height/2)
        self.screen.blit(TextSurf, TextRect)

    def puzzle_solved(self)-> None:
        # pause for effect!
        pg.time.delay(100)
        for row in range(self.g_height):
            for col in range(self.w_height):
                val = self.grid[row][col]
                self.draw_grid_square(row,col,val, GREEN)
        pg.display.flip()
        pg.time.delay(500)
        for row in range(self.g_height):
            for col in range(self.w_height):
                val = self.grid[row][col]
                self.draw_grid_square(row,col,val)
        pg.display.flip()
    
    def puzzle_failed(self)-> None:
        pg.time.delay(1000)
        message = "No solution possible :("
        delta = 2*self.margin
        rect_back = [self.width*1/9 - delta, 
                self.height*2/9 - delta,
                self.width*7/9 + 2*delta,
                self.height*5/9 + 2*delta]
        rect = [self.width*1/9, 
                self.height*2/9,
                self.width*7/9,
                self.height*5/9]       
        pg.draw.ellipse(self.screen, BLACK, rect_back)
        pg.draw.ellipse(self.screen, WHITE, rect)
        
        TextSurf, TextRect = text_objects(message, self.message_font, BLACK)
        TextRect.center = (self.width/2, self.height/2)
        self.screen.blit(TextSurf, TextRect)
        pg.display.flip()
        pg.time.delay(3000)



