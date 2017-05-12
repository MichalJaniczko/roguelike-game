def move(x_pos, y_pos, character, forestmap):
    """Function responsible for movement player,
    get paramet character and when it equal to "wasd" change
    position by defined value.
    Function prevent cross boarder of game area.
    """


    #forestmap[y_pos][x_pos] = "."
    if character == "w":
        if forestmap[y_pos - 1][x_pos] == ".":
            y_pos -= 1
    if character == "s":
        if forestmap[y_pos + 1][x_pos] == ".":
            y_pos += 1
    if character == "a":
        if forestmap[y_pos][x_pos - 1] == ".":
            x_pos -= 1
    if character == "d":
        if forestmap[y_pos][x_pos + 1] == ".":
            x_pos += 1
    return x_pos, y_pos

