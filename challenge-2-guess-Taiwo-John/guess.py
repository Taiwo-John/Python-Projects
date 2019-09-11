# Your name goes here :)
from aluLib import *

# I'm providing you with a general structure, but feel free to remove ALL
# OF IT and do it your way

CARD_WIDTH = 100
CARD_HEIGHT = 145
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
x_img = 20
y_img = 50

position = []
state = [0, 0, 0, 0, 0, 0]


# You will probably still need quite a few globals
cards = ['A', 'A', 'K', '2', '2', 'K']


# This function will draw the cards
def draw_cards():
    # remove the line below once you start working on this
    for card in range(len(cards)):
        if state[card] == 1:
            img = load_image('assets/' + cards[card])
            draw_image(img, x_img + card * (x_img + CARD_WIDTH), y_img)


# This function decides what should happen given the state of the cards
# Are there any cards we should remove? any cards we should hide?
# You won't need this until milestone 3

# Check the mouse input, and flip relevant cards
def check_mouse_input():
    # remove the line below once you start working on this
    if is_mouse_pressed():
        click_monitor = 1
        for n in range(len(cards)):
            if mouse_x() >= x_img + n * (x_img + CARD_WIDTH) and mouse_x() <= (n+1) *(x_img + CARD_WIDTH):
                if mouse_y() >= y_img and mouse_y() <= y_img + CARD_HEIGHT:
                    state[n] = 1
        print(state)


def check_card_state():
    # remove the line below once you start working on this
    for status in range(len(state)):
        if state[status] == 0:
            set_fill_color(0.5, 1, 0.75)
            draw_rectangle(x_img + status * (x_img + CARD_WIDTH), y_img, CARD_WIDTH, CARD_HEIGHT)
        elif state[status] == 1:
            draw_cards()


def main():
    # As mentioned, this is just a suggested structure. Feel free to change this if you prefer
    clear()
    draw_cards()
    check_card_state()
    check_mouse_input()


# Keep a low framerate to your submission. 10 worked well for me, but experiment on your own.
start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=10)