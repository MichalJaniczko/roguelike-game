with open("maps.txt", "r") as f:
    forestmap = f.readlines()
    for i in range(len(forestmap)):
        forestmap[i] = list(forestmap[i])



def create_board(width, height):
    """Function create game area (borders made with #),
    width and height are imput parameters define wer borders are made
    """
    board = []
    for row in range(0, height):
        board_row = []
        for column in range(0, width):
            if row == 0 or row == height - 1:
                board_row.append("#")
            else:
                if column == 0 or column == width - 1:
                    board_row.append("#")
                else:
                    board_row.append(" ")
        board.append(board_row)
    return board


def print_board(board):
    """Function print game area"""
    for line in forestmap:
        for char in line:
            if char == "&":
                char = '\033[92m' + "&" + '\x1b[0m'
            if char == "$":
                char = '\033[93m' + "$" + '\x1b[0m'
            print(char, end="")