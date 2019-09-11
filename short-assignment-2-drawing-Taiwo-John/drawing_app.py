# Taiwo John // Cohort 1
# Self Assignment 2: Drawing brush
# Disclaimer: This program is open to criticism as it helps to make it better :)


from aluLib import *

window_width = 800
window_height = 800
# You probably want another global variable for the size of the brush
size_of_brush = 20


# This function should check key presses, and determine what color we draw with next

def determine_color():
    # Checking if the 'r' or 'R' key is pressed and setting brush color to red
    if is_key_pressed('r'):
        set_fill_color(1, 0, 0)

    # Checking if the 'g' or 'G' key is pressed and setting brush color to green
    elif is_key_pressed('g'):
        set_fill_color(0, 1, 0)

    # Checking if the 'y' or 'Y' key is pressed and setting brush color to yellow
    elif is_key_pressed('y'):
        set_fill_color(1, 1, 0)

    # Checking if the 'e' or 'E' key is pressed and setting brush color to very light grey (in order to erase)
    elif is_key_pressed('e'):
        set_fill_color(0.94, 0.94, 0.94)

    # Adding the clear () function to clear the screen or reset if the 'c' or 'C' key is pressed
    elif is_key_pressed('c'):
        clear()

# This function should also check key presses, and determine how big the brush should be


def determine_brush_size():
    # Calling the global size_of_brush variable to modify it.
    global size_of_brush

    # Increasing the size_of_brush by 5 when the '+' key is pressed and setting the maximum size_of_brush to 100
    if is_key_pressed("+"):
        if size_of_brush <= 100:
            size_of_brush += 5

    # Decreasing the size_of_brush by 5 when the '-' key is pressed and setting the minimum size_of_brush to 5
    elif is_key_pressed("-"):
        if size_of_brush >= 5:
            size_of_brush -= 5


# This function should draw the brush when necessary
def draw():
    global size_of_brush
    if is_mouse_pressed():
        draw_circle(mouse_x(), mouse_y(), size_of_brush)


# This function calls all the other functions. I have renamed mine from main() to master_draw() for uniqueness :)
def master_draw():
    # This makes sure the circles we draw don't have a border
    disable_stroke()

    # Decide what color to draw with, or alternatively erase.
    determine_color()

    # Decide how big the brush should be
    determine_brush_size()

    # Draw if you should be drawing
    draw()


start_graphics(master_draw, width=window_width, height=window_height, framerate=60)
