import os
from gameInventory import*


def create_maps(name):
    """Function open and return map from name parameters"""
    with open(name, "r") as f:
        map_list = f.readlines()
        for i in range(len(map_list)):
            map_list[i] = list(map_list[i])
    return map_list


def print_board(map_list, inventory, name):
    """Function print game area and inventory"""
    for line in map_list:
        for char in line:
            if char == "🌴":
                char = '\033[92m' + "🌴" + '\x1b[0m'
            if char == ".":
                if name == 'forest.txt':
                    char = '\033[92m' + "." + '\x1b[0m'
                elif name == 'desert.txt':
                    char = '\033[93m' + "." + '\x1b[0m'
                elif name == 'maps_hoth.txt':
                    char = '\x1b[0;35;40m' + "." + '\x1b[0m'
            if char == "🍻":
                char = '\033[93m' + "🍻" + '\x1b[0m'
            if char == "🔪":
                char = '\033[91m' + "🔪" + '\x1b[0m'
            if char == "🍙":
                char = '\033[95m' + '🍙' + '\x1b[0m'
            if char == "🌊":
                char = '\033[94m' + "🌊" + '\x1b[0m'
            if char == "$":
                char = '\033[93m' + "$" + '\x1b[0m'
            if char == "#":
                char = '\033[93m' + "#" + '\x1b[0m'
            if char == "⛺️":
                char = '\033[93m' + "⛺️" + '\x1b[0m'
            if char == "🌵":
                char = '\033[92m' + "🌵" + '\x1b[0m'
            if char == "🔥":
                char = '\x1b[0;31;40m' + "🔥" + '\x1b[0m'
            print(char, end="")
    if len(inventory) == 0:
        print("No items in inventory")
    else:
        print_table(inventory, "count,desc")


def insert_player(map_list, x, y):
    """Function place player @ on board in place define by two parameters"""
    os.system("clear")
    with open('choosen_char.txt', "r") as f:
        player = f.readlines()
        map_list[y][x] = player[0]
        return map_list