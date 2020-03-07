from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN
from random import choice

from exceptions import GameOver, GameError
import helpers
import snek as sss


class GameState:
    def __init__(self, max_y, max_x):
        self.score = 0
        self.max_y = max_y
        self.max_x = max_x
        self.snek = sss.Snek(max_y//2, max_x//2)
        self.food_pos = helpers.generate_random_food_position(max_y-1, max_x-1)
        self.last_key = choice([KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN])
    
    def get_snek(self):
        return self.snek
    
    def get_score(self):
        return self.score
    
    def get_food_position(self):
        return self.food_pos
    
    def generate_new_food_position(self):
        new_food_pos = helpers.generate_random_food_position(self.max_y-1, self.max_x-1)
        snek_coords = self.snek.get_illegal_moves()

        # do not generate food inside a snek
        while new_food_pos in snek_coords:
            new_food_pos = helpers.generate_random_food_position(self.max_y-1, self.max_x-1)
        
        self.food_pos = new_food_pos

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

        border_coords = helpers.get_border_coordinates(self.max_y, self.max_x)
        snek_coords = self.snek.get_illegal_moves()

        if next_pos in border_coords:
            raise GameOver('ran into the wall')
        elif next_pos in snek_coords:
            raise GameOver('snek ate itself')
        else:
            if next_pos == self.food_pos:
                self.generate_new_food_position()
                self.snek.consume_food(*next_pos)
                self.score += 1
            else:
                self.snek.move(*next_pos)
    
        self.last_key = key
