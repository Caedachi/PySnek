from random import choice
import curses
import sys

from exceptions import GameOver, GameError
import helpers
import snek as sss
import state


DIRECTIONS = {
    curses.KEY_LEFT: "<",
    curses.KEY_RIGHT: ">",
    curses.KEY_UP: "^",
    curses.KEY_DOWN: "v"
}


def main(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(True)
    stdscr.timeout(100)  # adjust for difficulty

    max_y, max_x = stdscr.getmaxyx()
    game = state.GameState(max_y, max_x)

    while True:
        try:

            stdscr.clear()
            stdscr.refresh()

            stdscr.border()
            snek = game.get_snek()
            food_y, food_x = game.get_food_position()
            head_y, head_x = snek.get_head().get_position()
            score = game.get_score()

            for sneklet in snek.get_body():
                char = 'O'
                y, x = sneklet.get_position()
                if (y, x) == (head_y, head_x):
                    char = DIRECTIONS.get(game.get_last_key(), 'O')
                stdscr.addstr(y, x, char)
            stdscr.addstr(food_y, food_x, '@')
            stdscr.addstr(0, 1, str(score))

            key = stdscr.getch()

            if key == curses.KEY_RESIZE:
                continue
            elif key == ord('q'):
                raise GameOver("u quit") 
            else:
                game.next_state(key)
        except GameOver as e:
            stdscr.timeout(-1)
            stdscr.clear()
            stdscr.refresh()
            stdscr.border()
            stdscr.addstr(1, 1, 'game over snek: {}'.format(e))
            stdscr.addstr(2, 2, 'score: {}'.format(game.get_score()))
            stdscr.getch()
            sys.exit(0)


curses.wrapper(main)
