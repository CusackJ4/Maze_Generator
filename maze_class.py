from window_class import Window, Cell
from time import sleep
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols,
                cell_size_x, cell_size_y, win=None, seed = None,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        if seed != None:
             self.seed = random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

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
        if self.win != None:
            self.win.redraw()
            sleep(0.001)
    
    def __break_entrance_and_exit(self):
         self.__cells[0][0].has_top_wall = False
         self.__draw_cell(0, 0)

         exit_col = self.num_cols - 1
         exit_row = self.num_rows - 1
         self.__cells[exit_col][exit_row].has_bottom_wall = False
         self.__draw_cell(exit_col, exit_row)
         
    def __break_walls_r(self, i, j):
         self.__cells[i][j].visited = True 

         while True:
            to_visit = []
            directions = []

            if j - 1 >= 0: # top
                top_neighbour = self.__cells[i][j-1]
                if not top_neighbour.visited:
                     to_visit.append((i, j-1))
                     directions.append("top")
                     
            if i + 1 < self.num_cols:
                 right_neighbour = self.__cells[i+1][j]
                 if not right_neighbour.visited:
                      to_visit.append((i+1, j))
                      directions.append("right")
                      
            if j + 1 < self.num_rows: # bottom
                 bottom_neighbour = self.__cells[i][j+1]
                 if not bottom_neighbour.visited:
                      to_visit.append((i, j+1))
                      directions.append("bottom")
                      
            if i - 1 >= 0: # left edge
                 left_neighbour = self.__cells[i-1][j]
                 if not left_neighbour.visited:
                      to_visit.append((i-1, j))
                      directions.append("left")
                      
            if not to_visit: #break out of loop if no unvisited neighbours
                 self.__draw_cell(i, j)
                 return
            
            # Select 
            idx = random.randrange(len(to_visit)) # select index for direction to head
            next_i, next_j = to_visit[idx] # assign next coordinates to vars
            direction = directions[idx] # set direction for conditional

            # Break the wall between the current and chosen  cell
            if direction == "top":
                 self.__cells[i][j].has_top_wall = False
                 self.__cells[next_i][next_j].has_bottom_wall = False
            elif direction == "right":
                 self.__cells[i][j].has_right_wall = False
                 self.__cells[next_i][next_j].has_left_wall = False
            elif direction == "bottom":
                 self.__cells[i][j].has_bottom_wall = False
                 self.__cells[next_i][next_j].has_top_wall = False
            else: # left
                 self.__cells[i][j].has_left_wall = False
                 self.__cells[next_i][next_j].has_right_wall = False
                          
            # recursively visit the next cell
            self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):
         for col in self.__cells:
              for cell in col:
                   cell.visited = False

    def solve(self):
        self._solve_r(i = 0, j = 0)
    
    def _solve_r(self, i, j):
         self._animate()
         self.__cells[i][j].visited = True

         exit_col = self.num_cols - 1
         exit_row = self.num_rows - 1

         if self.__cells[i][j] == self.__cells[exit_col][exit_row]:
              return True

         if j - 1 >= 0: # Checks to see if cell is above
            if self.__cells[i][j].has_top_wall == False:
                 if self.__cells[i][j-1].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i][j-1], undo=False)
                    result = self._solve_r(i, j-1)
                    if result == False:
                        self.__cells[i][j].draw_move(self.__cells[i][j-1], undo=True)
                    else:
                        return 
         if i - 1 >= 0: # Checks to see if cell to left
            if self.__cells[i][j].has_left_wall == False:
                 if self.__cells[i-1][j].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i-1][j], undo=False)
                    result = self._solve_r(i-1, j)
                    if result == False:
                        self.__cells[i][j].draw_move(self.__cells[i-1][j], undo=True)  
                    else:
                        return
         if i + 1 < self.num_cols: # Check cell right
            if self.__cells[i][j].has_right_wall == False:
                 if self.__cells[i+1][j].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i+1][j], undo=False)
                    result = self._solve_r(i+1, j)
                    if result == False:
                        self.__cells[i][j].draw_move(self.__cells[i+1][j], undo=True)
                    else:
                        return
         if j + 1 < self.num_rows: # Check cell bottom
            if self.__cells[i][j].has_bottom_wall == False:
                 if self.__cells[i][j+1].visited == False:
                    self.__cells[i][j].draw_move(self.__cells[i][j+1], undo=False)
                    result = self._solve_r(i, j+1)
                    if result == False:
                        self.__cells[i][j].draw_move(self.__cells[i][j+1], undo=True)
                    else:
                        return

         return False  
         
         


         


# print("Maze class file loaded successfully", Maze)
# print("Imported Cell:", Cell)





