# -*- coding: utf-8 -*-
import os
from load_maps import*
from load_menu import*


def main():
    print_menu_boards('menu.txt')
    chose_char("chose.txt")
    dic_item = {}
    inventory = forestmap(dic_item)
    desertmap(inventory)
    maps_hoth(inventory)
    boss_attack(x_pos, y_pos, character, map_hoth)

if __name__ == "__main__":
    main()
