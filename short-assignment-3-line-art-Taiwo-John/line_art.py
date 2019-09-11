# Taiwo John Short Assignment 3.
# Creating a line art.
from aluLib import *

# Don't forget you must create an additional function. Go check out the instructions!

# Parameters that contain an x represent x coordinates, and y represent y coordinates
# Parameters with a 1 define the first line, parameters with a 2 define the second
# x1a and y1a define 1 point together, same for x2a and y2a etc.


def draw_line_art(x1a, y1a, x1b, y1b, x2a, y2a, x2b, y2b, line_count):
    # This draws the black background to fill up the window screen.
    set_fill_color(0, 0, 0)
    draw_rectangle(0, 0, 500, 500)

    # Setting the color for the line strokes.
    set_stroke_color(0, 0, 1)
    # The next two draw_line functions draw the first two base lines.
    draw_line(x1a, y1a, x1b, y1b)
    draw_line(x2a, y2a, x2b, y2b)

    # These variables compute coordinates of the 1/(line_count -1) points of the two lines.
    # for example, if line_count = 3, they compute the coordinates of the 1/2(mid) point of the two lines.
    # This only works if our line_count is greater than 1, because if it is equal to 1, we will be dividing by zero
    # which is undefined.
    divide_x1 = 0
    divide_y1 = 0
    divide_x2 = 0
    divide_y2 = 0
    if line_count > 1:
        divide_x1 = (x1b - x1a) / (line_count - 1)
        divide_y1 = (y1b - y1a) / (line_count - 1)
        divide_x2 = (x2a - x2b) / (line_count - 1)
        divide_y2 = (y2a - y2b) / (line_count - 1)

    # This loops the number of line we draw according to the parameters we give when we call the draw_line_art function
    count = 0
    while line_count > 0:
        draw_line(x1a + count * divide_x1, y1a + count * divide_y1,  x2b + count * divide_x2, y2b + count * divide_y2)

        # The count variable counts the number of connecting lines we have drawn in sequence.
        # Count starts from zero and is incremented by 1, for example, after we draw the first line, count becomes 1.
        count += 1
        # We also decrease the line count variable by 1, to check the number of lines we still need to draw.
        line_count -= 1


# This function takes three values; start_value, end_value, line_count. It returns a list with the start_value, the
# intermediate values needed to create additional lines up to line_count, and the end_value.
def _get_intermediate_values_(start_value, end_value, line_count):
    # Creating the variable in which I want to store the returned list.
    inter_values = []

    if line_count > 0:
        list_count = 0

        # val computes the intermediate points. val is multiplied by list_count, according to the number of lines we
        # want to draw.
        val = (end_value - start_value)//(line_count-1)
        while list_count < line_count - 1:
            inter_values.append(start_value + list_count * val)
            list_count += 1
    inter_values.append(end_value)
    return inter_values


# The main function is defined to call the draw_line_art function, with given parameters.
def main():
    # Start some line art, the first 4 parameters represent the coordinates of 2 points, which define a line
    # The next 4 coordinates also represent 2 points, which define a second line
    # The final parameter represents how many partial lines are desired
    draw_line_art(350, 50, 20, 80, 350, 300, 40, 220, 50)


start_graphics(main)