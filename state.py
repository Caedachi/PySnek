from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
from random import choice

from exceptions import GameOver, GameError
import helpers
import snek as sss


class GameState:
    def __init__(self, max_y: int, max_x: int):
        self.score = 0
        self.max_y = max_y
        self.max_x = max_x
        self.snek = sss.Snek(max_y//2, max_x//2)
        self.last_key = choice([KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN])

        self.border_coords = helpers.get_border_coordinates(self.max_y, self.max_x)
        gameboard = helpers.get_gameboard_coordinates(self.max_y, self.max_x)
        self.playable_area = helpers.get_playable_area(self.border_coords, gameboard)

        self.food_pos = helpers.get_random_food_position(self.playable_area, self.snek.get_illegal_moves())
    
    def get_snek(self):
        return self.snek
    
    def get_score(self):
        return self.score
    
    def get_food_position(self):
        return self.food_pos
    
    def generate_new_food_position(self):
        snek_coords = self.snek.get_illegal_moves()
        snek_coords.add(self.snek.get_tail().get_position())
        
        self.food_pos = helpers.get_random_food_position(self.playable_area, snek_coords)

    def get_last_key(self):
        return self.last_key

    def next_state(self, key):
        cur_y, cur_x = self.snek.get_head().get_position()

        if ((key == -1) or
            (self.last_key == KEY_LEFT and key == KEY_RIGHT) or
            (self.last_key == KEY_RIGHT and key == KEY_LEFT) or
            (self.last_key == KEY_UP and key == KEY_DOWN) or
            (self.last_key == KEY_DOWN and key == KEY_UP)):
            key = self.last_key

        next_pos = helpers.get_next_position(cur_y, cur_x, key)

        if next_pos in self.border_coords:
            raise GameOver('ran into the wall')
        elif next_pos in self.snek.get_illegal_moves():
            raise GameOver('snek ate itself')
        else:
            if next_pos == self.food_pos:
                self.generate_new_food_position()
                self.snek.consume_food(*next_pos)
                self.score += 1
            else:
                self.snek.move(*next_pos)
    
        self.last_key = key
