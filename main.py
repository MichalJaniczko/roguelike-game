from get_char import getch
from movment import move
from player import insert_player
from board import *
from random import randint
import os


def main():
    x_pos = 5
    y_pos = 15
    character = ""
    while character != "\\":
        character = getch()
        os.system("clear")
        x_pos, y_pos = move(x_pos, y_pos, character, forestmap)
        board_with_player = insert_player(forestmap, x_pos, y_pos)
        print_board(board_with_player)

if __name__ == "__main__":
    main()