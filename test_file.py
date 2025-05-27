import os
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir('.'))



from window_class import Window
# print("Window imported successfully")

from window_class import Cell  
# print("Cell imported successfully")

from maze_class import Maze
# print("Maze imported successfully")

win = Window(800, 600)
maze_test = Maze(0, 0, 2, 2, 50, 50, win)
maze_test._animate()
win.wait_for_close()