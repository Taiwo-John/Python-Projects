# Taiwo John Cohort 1
# Challenge 1 - Pong
# Open to thorough feedback :)

from aluLib import *

# Defining and Initializing variables
window_width, window_height = 1000, 700

# pad_1_x and pad_1_y = Left paddle x and y coordinates, # pad_2_x and pad_2_y = Right paddle x and y coordinates
pad_1_x, pad_1_y, pad_2_x, pad_2_y = 0, 0, window_width - 20, 0

# rec_width and rec_height = width and height of paddles respectively
rec_width, rec_height = window_width//50, window_width//6

# ball_cent_x and ball_cent_y = x and y coordinates of ball center, rad = radius of the ball
ball_cent_x, ball_cent_y, rad = window_width//2, window_height//2, 15

# speed_x and speed_y = Distance increment per frame rate of the ball on x and y axis, start = boolean to start the game
speed_x, speed_y, start = 5, 5, False


def draw_rect():
    global pad_1_y, pad_2_y
    # Drawing Border Line
    set_fill_color(0, 0, 1)
    draw_rectangle(window_width//2, 0, window_width//250, window_height)

    # Drawing First Rectangle
    set_fill_color(1, 1, 0)
    draw_rectangle(pad_1_x, pad_1_y, rec_width, rec_height)

    # Checking to see if Keys 'k' and 'm' is pressed to move the right paddle and also limit it to the screen
    if is_key_pressed('a'):
        if pad_1_y > 0:
            pad_1_y -= 5
    elif is_key_pressed('z'):
        if pad_1_y < window_height - 125:
            pad_1_y += 5

    # Drawing Second rectangle
    set_fill_color(1, 0, 0)
    draw_rectangle(pad_2_x, pad_2_y, rec_width, rec_height)

    # Checking to see if Keys 'k' and 'm' is pressed to move the right paddle and also limit it to the screen
    if is_key_pressed('k'):
        if pad_2_y > 0:
            pad_2_y -= 5
    if is_key_pressed('m'):
        if pad_2_y < window_height - 125:
            pad_2_y += 5


# Drawing the Ball
def draw_ball():
    set_fill_color(0, 1, 0)
    draw_circle(ball_cent_x, ball_cent_y, rad)


# Moving the ball
def move_bounce_ball():
    # Calling the variables by adding 'global' to make them able to be modified
    global start, ball_cent_x, ball_cent_y, speed_x, speed_y
    # Checking if the space key is pressed to start the game with the ball in the center
    if is_key_pressed(' '):
        ball_cent_x = window_width//2
        ball_cent_y = window_height//2
        start = True

    # Checking if the 'q' key is pressed to quit the game
    elif is_key_pressed('q'):
        cs1_quit()

    # If Start is pressed, the ball distance is increased, aka the ball moves
    if start:
        ball_cent_x += speed_x
        ball_cent_y += speed_y

        # This Checks if the ball touches the horizontal  sides, it makes it bounce back in opposite direction
        if ball_cent_y + rad == window_height or ball_cent_y - rad == 0:
            speed_y *= -1
        # This checks if the ball touches the vertical sides, it stops the ball, aka ends the game
        if ball_cent_x + rad == window_width or ball_cent_x - rad == 0:
            start = False
        # This checks if the ball touches the right paddle (aka paddle 1) to make it bounce off it
        if (ball_cent_y - rad >= pad_2_y and ball_cent_y + rad <= pad_2_y + rec_height) and ball_cent_x + rad == pad_2_x:
            speed_x *= -1
        # This checks if the ball touches the left paddle (aka paddle 2) to make it bounce off it
        if (ball_cent_y - rad >= pad_1_y and ball_cent_y + rad <= pad_1_y + rec_height) and ball_cent_x - rad == rec_width:
            speed_x *= -1


# All other functions are called in this main function
def main():
    clear()
    draw_rect()
    draw_ball()
    move_paddle_bounce_ball()


# This function takes in the main function to start the game
start_graphics(main, framerate=60, width=window_width, height=window_height)
