from aluLib import *

CARD_WIDTH = 100
CARD_HEIGHT = 145
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

x = 50
y = 150

cards = ['A', 'A', 'K', '2', '2', 'K']  # cards
recs = [0, 0, 0, 0, 0, 0]  # This list represents the hidden the cards
# This variables will be used to compare to clicked cards and
# we made sure to you use a number large than the size of our cards' list
first = 9
second = 9


def draw_cards():
    x = 50
    y = 150
    i = 0  # i is represents the index of cards member

    while i <= len(cards) - 1:
        if recs[i] == 0:
            set_fill_color(1, 0, 0)
            draw_rectangle(x, y, CARD_WIDTH, CARD_HEIGHT)
        elif recs[i] == 1:
            draw_image("assets/" + cards[i] + ".png", x, y)
        i = i + 1
        x = x + 120


def check_card_state():
    # remove the line below once you start working on this
    # This condition will check if variables first and second are not equal to 9
    # also if cards lists with index of variable first  and cards list with index of variable second and also
    # check if variable first and second are equal if the conditions are true
    #  then it will flip cards that meets the condtions according to the mouse input
    if first != 9 and second != 9 and cards[first] == cards[second] and first != second:
        recs[first] = 2
        recs[second] = 2


def check_mouse_input():
    global first, second
    i = 0
    x = 50
    if is_mouse_pressed():
        while i < len(cards):
            if recs[i] != 2:
                if x < mouse_x() < x + CARD_WIDTH and y < mouse_y() < (y + CARD_HEIGHT):
                    recs[i] = 1
                    first = second
                    second = i
                else:
                    recs[i] = 0
            i += 1
            x = x + 120


def main():
    clear()
    draw_cards()
    check_card_state()
    check_mouse_input()


start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=10)