def insert_player(forestmap, x, y):
    """Function place player @ on board in place define by two parameters"""
    forestmap[y][x] = '@'
    return forestmap