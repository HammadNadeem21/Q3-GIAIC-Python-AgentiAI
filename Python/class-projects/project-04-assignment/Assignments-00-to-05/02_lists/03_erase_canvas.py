# Problem Statement
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


# TK, for creating a window
# Canvas, for creating a shapes
from tkinter import Tk, Canvas

Canvas_width = 400
Canvas_hieght= 400
cell_size = 40
ereaser_size = 20

root = Tk()
canvas = Canvas(root, width=Canvas_width, height=Canvas_hieght, bg="white")
canvas.pack()

# create blue square
cells = []
for row in range(Canvas_hieght // cell_size):
    for col in range(Canvas_width // cell_size):
        x1, y1 = col * cell_size, row * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        cell = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
        cells.append(cell)

# for creating eraser
eraser = canvas.create_rectangle(0, 0, ereaser_size, ereaser_size, fill="pink")


def erase(event):
    x, y = event.x, event.y
    canvas.moveto(eraser, x, y)
    overlapping = canvas.find_overlapping(x, y, x + ereaser_size, y + ereaser_size)
    for obj in overlapping:
        if obj != eraser:
            canvas.itemconfig(obj, fill="white")


canvas.bind("<B1-Motion>", erase)


root.mainloop()
