from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN

from random import choice
from typing import Set, Tuple


def get_random_food_position(playable_area: Set[tuple], snek_coords: Set[tuple]) -> Tuple[int]:
    return choice(list(playable_area - snek_coords))

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

def get_border_coordinates(max_y, max_x) -> Set[tuple]:
    coords = []
    coords += [(i, 0) for i in range(max_y)]
    coords += [(0, i) for i in range(max_x)]
    coords += [(max_y-1, i) for i in range(max_x)]
    coords += [(i, max_x-1) for i in range(max_y)]

    return set(coords)

def get_gameboard_coordinates(max_y: int, max_x: int) -> Set[tuple]:
    coords = []
    for x in range(max_x):
        for y in range(max_y):
            coords.append((y, x))
    
    return set(coords)

def get_playable_area(border: Set[tuple], gameboard: Set[tuple]) -> Set[tuple]:
    return gameboard - border
