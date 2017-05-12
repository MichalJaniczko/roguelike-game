from print_board import*
from movment import*


def forestmap(inventory):
    """
    open forest.txt (1st map) insert player into position 5,5
    printing map, clearing map until we dont go into next map
    """
    forestmap = create_maps("forest.txt")
    x_pos = 5
    y_pos = 5
    forestmap = insert_player(forestmap, x_pos, y_pos)
    print_board(forestmap, inventory, 'forest.txt')
    while True:
        x_pos, y_pos = move(x_pos, y_pos, forestmap, inventory)
        if x_pos == "dupa" and y_pos == "dupa":
            break
        else:
            os.system("clear")
            forestmap = insert_player(forestmap, x_pos, y_pos)
            print_board(forestmap, inventory, 'forest.txt')
    return inventory


def desertmap(inventory):
    """
    open desertmap.txt (2nd map) insert player into position 5,5
    printing map, clearing map until we dont go into next map
    """
    desertmap = create_maps("desert.txt")
    x_pos = 5
    y_pos = 5
    desertmap = insert_player(desertmap, x_pos, y_pos)
    print_board(desertmap, inventory, 'desert.txt')
    while True:
        x_pos, y_pos = move(x_pos, y_pos, desertmap, inventory)
        if x_pos == "dupa" and y_pos == "dupa":
            break
        else:
            os.system("clear")
            desertmap = insert_player(desertmap, x_pos, y_pos)
            print_board(desertmap, inventory, 'desert.txt')
    return inventory


def maps_hoth(inventory):
    """
    open desertmap.txt (4tf map) insert player into position 5,5
    printing map, clearing map until we dont start boss fight
    """
    maps_hoth = create_maps("maps_hoth.txt")
    x_pos = 5
    y_pos = 5
    maps_hoth = insert_player(maps_hoth, x_pos, y_pos)
    print_board(maps_hoth, inventory, 'maps_hoth.txt')
    while True:
        x_pos, y_pos = move(x_pos, y_pos, maps_hoth, inventory)
        if x_pos == "dupa" and y_pos == "dupa":
            break
        else:
            os.system("clear")
            desertmap = insert_player(maps_hoth, x_pos, y_pos)
            print_board(maps_hoth, inventory, 'maps_hoth.txt')
    return inventory
