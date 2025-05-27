from window_class import Window, Cell
from maze_class import Maze
from time import sleep




if __name__ == "__main__":
    win = Window(800, 600)
    maze_test = Maze(0, 0, 4, 4, 50, 50, win)
    maze_test._animate()
    
    win.wait_for_close()

#     # win.draw_line(Line(Point(0, 0), Point(100, 100)), "black")
#     # cel = Cell(win)
#     # cel.draw(10, 100, 10, 100)
#     # cel2 = Cell(win)
#     # cel2.draw(100, 150, 100, 180)
#     # cel.draw_move(cel2, undo=True)