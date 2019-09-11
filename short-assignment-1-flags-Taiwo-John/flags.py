# Taiwo Temidayo John
# Self-Assignment 1: Drawing the flags of Benin, Guinea and Niger
# Disclaimer: No disrespect meant by starting the function names of countries in small letters, python made me do it :)

from aluLib import *

window_width = 1500
window_height = 900


# Note that functions are expected to be lowercase, so don't be tempted to capitalize


def benin():  # Defining the function 'benin'

    # Because there are 3 rectangles; one vertical and two horizontal ones, I defined the following variables:
    # Width and height of the horizontal rectangle and width of the vertical rectangle

    width_vert_rect = window_width / 3
    width_hor_rect = window_width - width_vert_rect
    height_hor_rect = window_height / 2

    # Setting the color and drawing the first (greenish-vertical) rectangle on the left side

    set_fill_color(0, 0.6, 0.35)
    draw_rectangle(0, 0, width_vert_rect, window_height)

    # Setting the color and drawing the second (yellowish-horizontal) rectangle on the topmost right side

    set_fill_color(1, 1, 0.12)
    draw_rectangle(width_vert_rect, 0, width_hor_rect, height_hor_rect)

    # Setting the color and drawing the third (red-horizontal) rectangle on the bottom right side

    set_fill_color(0.8, 0, 0.1)
    draw_rectangle(width_vert_rect, height_hor_rect, width_hor_rect, height_hor_rect)


def guinea():  # Defining the function 'guinea'

    # Because there are 3 rectangles of nearly equal width, I defined the variable width_rectangle by dividing the
    # window width into 3

    width_rectangle = window_width / 3

    # Setting the color and drawing the first (red) rectangle on the left side

    set_fill_color(0.8, 0, 0.1)
    draw_rectangle(0, 0, width_rectangle, window_height)

    # Setting the color and drawing the second (yellowish) rectangle in the middle

    set_fill_color(1, 1, 0.12)
    draw_rectangle(width_rectangle, 0, width_rectangle, window_height)

    # Setting the color and drawing the third (greenish) rectangle on the right side

    set_fill_color(0, 0.6, 0.35)
    draw_rectangle(width_rectangle * 2, 0, width_rectangle, window_height)


def niger():  # Defining the function 'niger'

    # There are two rectangles that are about one-third of the flag height. I have set their heights below:

    height_rectangle = window_height / 3

    # Setting the color and drawing the first (orange-colored) rectangle at the top

    set_fill_color(1, 0.38, 0.12)
    draw_rectangle(0, 0, window_width, height_rectangle)

    # Setting the color and drawing the circle in the middle

    set_fill_color(1, 0.38, 0.12)
    draw_circle(window_width / 2, window_height / 2, window_width / 10 - 20)

    # Setting the color and drawing the second (greenish) rectangle at the bottom

    set_fill_color(0, 1, 0.23)
    draw_rectangle(0, height_rectangle * 2, window_width, height_rectangle)


# Calling the function 'guinea'. Other functions in this program can be called by substituting the function name.
start_graphics(guinea, width=window_width, height=window_height)
