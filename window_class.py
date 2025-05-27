from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Filler Title")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()  # Process all pending idle tasks
        self.__root.update()  # Process all pending events

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()

    def draw_line(self, line, fill_colour):
        line.draw(self.__canvas, fill_colour)

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_colour):
        canvas.create_line(
                self.point_1.x_coord, self.point_1.y_coord, self.point_2.x_coord, self.point_2.y_coord,
                fill=fill_colour, width=2
            )
        
class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black") # left wall
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black") # right wall
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black") # tops wall
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black") # bottom wall

    def calc_centre(self):
        self.centre_x  = (self.__x1 + self.__x2)/2
        self.centre_y  = (self.__y1 + self.__y2)/2
        return self.centre_x, self.centre_y
    
    def draw_move(self, to_cell, undo=False):
        colour = "red" if undo == False else "gray"
        self.__win.draw_line(Line(Point(*self.calc_centre()), Point(*to_cell.calc_centre())), colour) # * is for tuple unpacking


