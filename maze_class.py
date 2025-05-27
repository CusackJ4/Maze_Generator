from window_class import Window, Cell
from time import sleep

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols,
                cell_size_x, cell_size_y, win,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]        
        
        
        for col in range(self.num_cols):
                for row in range(self.num_rows):
                    self.__draw_cell(col, row) 

    def __draw_cell(self, i, j):
        self.one_cell = self.__cells[i][j]
        self.one_cell.draw(self.x1 + (i * self.cell_size_x), self.x1 + ((i + 1) * self.cell_size_x), 
                           self.y1 + (j * self.cell_size_y), self.y1 + ((j + 1) * self.cell_size_y))
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)

print("Maze class file loaded successfully", Maze)
print("Imported Cell:", Cell)





