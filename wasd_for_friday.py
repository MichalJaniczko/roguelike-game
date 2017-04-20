from random import randint
from time import sleep
import os


def create_board(width, height):
    board = []
    for row in range(0, height):
        board_row = []
        for column in range(0, width):
            if row == 0 or row == height - 1:
                board_row.append("X")
            else:
                if column == 0 or column == width - 1:
                    board_row.append("X")
                else:
                    board_row.append(" ")
        board.append(board_row)
    return board


def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')
        print()


def insert_player(board, width, height):
    board[height][width] = '@'
    return board


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def move(x_pos, y_pos, character):
    if character == "w" and y_pos > 1:
        y_pos -= 1
    if character == "s" and y_pos < 18:
        y_pos += 1
    if character == "a" and x_pos > 1:
        x_pos -= 1
    if character == "d" and x_pos < 58:
        x_pos += 1
    return x_pos, y_pos


def main():
    x_pos = 5
    y_pos = 15
    character = ""
    while character != "\\":
        character = getch()
        os.system("clear")
        board = create_board(60, 20)
        x_pos, y_pos = move(x_pos, y_pos, character)
        board_with_player = insert_player(board, x_pos, y_pos)
        print_board(board_with_player)


main()
