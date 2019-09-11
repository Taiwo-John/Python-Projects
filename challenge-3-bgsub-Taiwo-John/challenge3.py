# Taiwo John
# Challenge 3 - Background Substitution.
from aluLib import *

# Defining Variables
# Asking the user to input the names of the image files they want to modify and replace with
fore_img = str(input('Please enter the name of the front/fore image:\n'))
initial_background = str(input('Please enter the name of the initial background image:\n'))
desired_background = str(input('Please enter the name of the desired background image:\n'))

# Loading the input files and storing them in variables using the load_image function.
front_img = load_image(fore_img)
init_back_img = load_image(initial_background)
second_back_img = load_image(desired_background)

# Defining height and with variables
window_width = 1200
width = front_img.width()
height = front_img.height()


# The chromakey function
def chromakey():
    # Creating a copy of the front image.
    new_image = front_img.copy()
    # Looping through all the coordinates of the fore/front image and the desired background image to store their pixels
    for pos_x in range(width):
        for pos_y in range(height):
            fore_pi = front_img.get_pixel(pos_x, pos_y)
            back_pi = second_back_img.get_pixel(pos_x, pos_y)
            # Checking to see if the pixel of the front/fore image is 'green' enough and then replacing it with
            # the pixel of the desired background image.
            if fore_pi[0] < fore_pi[1] > fore_pi[2]:
                new_image.set_pixel(pos_x, pos_y, back_pi[0], back_pi[1], back_pi[2])
    # Drawing the image, saving it, and also, drawing a text to indicate that it is chromakey function.
    draw_text('Chroma Key', width + 20, 150)
    new_image.save('output_chroma.jpg')
    draw_image(new_image, 0, 0)


# The background Substitution function
def background_sub():
    # Importing the python math function as it will be used in this function.
    import math
    # Creating a copy of the front image
    new_image = front_img.copy()
    # Looping through the coordinates of the fore/front image, the initial background image and the desired background
    # image to store their pixels.
    for pos_x in range(width):
        for pos_y in range(height):
            fore_pi = front_img.get_pixel(pos_x, pos_y)
            back_1_pi = init_back_img.get_pixel(pos_x, pos_y)
            back_2_pi = second_back_img.get_pixel(pos_x, pos_y)
            # Computing the distance between the pixels of the fore image and the initial background image
            distance = math.sqrt(pow((fore_pi[0] - back_1_pi[0]), 2) + pow((fore_pi[1] - back_1_pi[1]), 2) + pow((fore_pi[0] - back_1_pi[0]), 2))
            # Checking to see if the distance between the pixels of the fore image and the initial background image are
            # close enough. (Here, I used 0.5 as the benchmark for a 'close enough' distance.
            # If the distance between the pixels are close enough, it means they are from the initial background and
            # they are replaced with the new background image pixels.
            if distance < 0.5:
                new_image.set_pixel(pos_x, pos_y, back_2_pi[0], back_2_pi[1], back_2_pi[2])
    # Drawing the image, saving it, and also, drawing a text to indicate that it is the Background Substitution function
    new_image.save('output_bgsub.jpg')
    draw_text('Background_Substitution', 2 * width + 200, 150)
    draw_image(new_image, width + 150, 0)


# Defining a main function in which both functions will be called.
def main():
    chromakey()
    background_sub()


# Calling the start_graphics function to draw the images at a rate of 50 times per second.
start_graphics(main, framerate=50, width=window_width, height=height)