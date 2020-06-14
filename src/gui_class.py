import pygame as pg

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

class Gui:
    def __init__(self, model):
        self.grid = model
        self.g_height = len(model)
        self.w_height = len(model[0])  

        # initialise the display
        # set up pygame
        pg.init()

        # set dimensions
        self.rect_height, self.rect_width, self.margin  = 140, 140, 3
        self.total_rect_height, self.total_rect_width   = tuple(map(lambda x: 2*self.margin+x, (self.rect_height, self.rect_width))) 
        self.winsize = self.width, self.height          = tuple(map(lambda x: x*9, (self.total_rect_width, self.total_rect_height)))

        # set up the screen and font
        self.screen = pg.display.set_mode(self.winsize, 0, 32)
        self.screen.fill(BLACK)
        self.font = pg.font.Font("resources/Roboto-Regular.ttf", 80)
        pg.display.set_caption('Sudoku')

        for row in range(self.g_height):
            for col in range(self.w_height):
                val = self.grid[row][col]
                self.draw_grid_square(row,col,val)
        pg.display.flip()

    def update_square(self, row, col, val): 
        self.draw_grid_square(row,col,val)
        pg.display.flip()

    def draw_grid_square(self, row, col, val):
        txt = ""
        if val is None:
            txt = "X"
        else:
            txt = str(val)
        colour = WHITE
        rect = [(2*self.margin + self.rect_width)*col + self.margin, 
                (2*self.margin + self.rect_height)*row + self.margin, 
                self.rect_width,
                self.rect_height]
        pg.draw.rect(self.screen, colour, rect)
        TextSurf, TextRect = text_objects(txt, self.font)
        TextRect.center = (rect[0] + self.total_rect_width/2, rect[1] + self.total_rect_height/2)
        self.screen.blit(TextSurf, TextRect)