import os
from movment import getch


def print_menu_boards(menu_name):
    """ Function responsible for prints in menu board"""
    button = ""
    while not button == "j":
        os.system("clear")
        with open(menu_name, 'r') as menu:
            menu = menu.readlines()
            for i in range(len(menu)):
                print(menu[i], end="")
        button = getch()
        if button == 'p':
            menu_name = 'gameinfo.txt'
            os.system("clear")
        elif button == 'o':
            menu_name = 'author.txt'
            os.system("clear")
        elif button == 'k':
            menu_name = 'storyline.txt'
            os.system("clear")
        elif button == 'm':
            menu_name = 'menu.txt'
            os.system("clear")
        elif button == 'x':
            os.system("clear")
            exit()


def chose_char(choose):
    """
    Function create a file, save character choice into it and name.
    Got always 2 string separated by spacebar
    """
    os.system("clear")
    with open(choose, 'r') as choose_char:
        choose_cha = choose_char.readlines()
        for i in range(len(choose_cha)):
            print(choose_cha[i], end="")
    button = getch()
    if button == "1":
        with open('choosen_char.txt', "w") as choosen_char:
            choosen_char.write('\x1b[0;32;40m@\x1b[0m')
    elif button == "2":
        with open('choosen_char.txt', "w") as choosen_char:
            choosen_char.write('\033[95m#\x1b[0m')