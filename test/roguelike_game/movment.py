from gameInventory import*
from hot_cold import*


def getch():
    """Function take imput key and return it in "ch"""
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def move(x_pos, y_pos, map_list, inventory):
    """
    Function responsible for movement player,
    get paramet character and when it equal to "wasd" change
    position by defined value.
    Function prevent cross boarder of game area.
    Also responsible for pick up items
    """
    boss_build = ["/", "|", "\\", "<", ">", "_", "~"]
    items = {"$": "COINS", "🌀": "POWER SYMBOL", "🐜": "FOOD", "🍻": "BEER", "🔪": "LIGHTSABER"}
    map_list[y_pos][x_pos] = "."
    character = getch().lower()

    if character == "w":
        if map_list[y_pos - 1][x_pos] == ".":
            y_pos -= 1
        elif map_list[y_pos - 1][x_pos] in items.keys():
            y_pos -= 1
            add_to_inventory(inventory, items[map_list[y_pos][x_pos]])
            map_list[y_pos][x_pos] == '.'
        elif map_list[y_pos - 1][x_pos] in boss_build:
            x_pos -= 1
            boss_attack(x_pos, y_pos, character, map_list)

    if character == "s":
        if map_list[y_pos + 1][x_pos] == ".":
            y_pos += 1
        elif map_list[y_pos + 1][x_pos] in items.keys():
            y_pos += 1
            add_to_inventory(inventory, items[map_list[y_pos][x_pos]])
            map_list[y_pos][x_pos] == '.'
        elif map_list[y_pos + 1][x_pos] in boss_build:
            y_pos += 1
            boss_attack(x_pos, y_pos, character, map_list)

    if character == "a":
        if map_list[y_pos][x_pos - 1] == ".":
            x_pos -= 1
        elif map_list[y_pos][x_pos - 1] in items.keys():
            x_pos -= 1
            add_to_inventory(inventory, items[map_list[y_pos][x_pos]])
            map_list[y_pos][x_pos] == '.'
        elif map_list[y_pos][x_pos - 1] in boss_build:
            x_pos -= 1
            boss_attack(x_pos, y_pos, character, map_list)

    if character == "d":
        if map_list[y_pos][x_pos + 1] == ".":
            x_pos += 1
        elif map_list[y_pos][x_pos + 1] in items.keys():
            x_pos += 1
            add_to_inventory(inventory, items[map_list[y_pos][x_pos]])
            map_list[y_pos][x_pos] == '.'
        elif map_list[y_pos][x_pos + 1] in boss_build:
            x_pos += 1
            boss_attack(x_pos, y_pos, character, map_list)

        elif map_list[y_pos][x_pos + 1] == "D":
            if inventory.get("FOOD") is not None and inventory.get("FOOD") >= 2:
                inventory["FOOD"] = inventory["FOOD"] - 2
                return "dupa", "dupa"
        elif map_list[y_pos][x_pos + 1] == "P":
            if inventory.get("BEER") is not None and inventory.get("BEER") >= 1:
                inventory["BEER"] = inventory["BEER"] - 1
                return "dupa", "dupa"

    if character == "\\":
        exit()

    return x_pos, y_pos


def boss_attack(x_pos, y_pos, character, map_list):
    """ Ending game, and printing lose/win screen"""
    fight = boss_fight()
    fight[0]
    if fight[1] == 1:
        exit()