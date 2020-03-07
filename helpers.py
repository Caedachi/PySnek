from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN

from random import randint


def generate_random_food_position(max_y, max_x):
    return (randint(1, max_y - 1), randint(1, max_x - 1))

def get_next_position(cur_y, cur_x, key):
    if key == KEY_LEFT:
        cur_x -= 1
    elif key == KEY_RIGHT:
        cur_x += 1
    elif key == KEY_UP:
        cur_y -= 1
    elif key == KEY_DOWN:
        cur_y += 1

    return (cur_y, cur_x)

def get_border_coordinates(max_y, max_x):
    coords = []
    coords += [(i, 0) for i in range(max_y)]
    coords += [(0, i) for i in range(max_x)]
    coords += [(max_y-1, i) for i in range(max_x)]
    coords += [(i, max_x-1) for i in range(max_y)]

    return set(coords)
