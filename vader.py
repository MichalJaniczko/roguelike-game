def open_vader():
    with open("vader.txt", "r") as v:
        vader = f.readlines()
        for i in range(len(vader)):
            vader[i] = list(vader[i])
        return vader


def insert_boss(forestmap, x, y):
    """Function place player @ on board in place define by two parameters"""
    vader = open_vader()
    forestmap[y][x] = vader
    return forestmap

print(open_vader())