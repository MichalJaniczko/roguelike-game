from random import randint
import os



def drawing_number():
    first = randint(1, 9)
    second = randint(0, 9)
    while second != first:
        break
    else:
        second = randint(0, 9)
    third = randint(0, 9)
    while third != second and third != first:
        break
    else:
        third = randint(0, 9)
    number = str(first)+str(second)+str(third)
    return number


def check():
    guessing = 1
    while guessing == 1:
        guess = input('input three digital number' + '\n')
        try:
            int(guess)
            if len(guess) == 3:
                return guess
        except ValueError:
            print("It's not a number")


def print_endgame(menu_name):
    os.system("clear")
    with open(menu_name, 'r') as menu:
        menu = menu.readlines()
        for i in range(len(menu)):
            print(menu[i], end="")
        print("")


def guess():
    os.system("clear")
    won = 0
    number = drawing_number()
    print(number)
    life = 3
    while life > 0:
        clue = []
        guess = check()
        if guess == number:
            won = 1
            win = print_endgame("win.txt")
            return win, won
        else:
            for i in range(0, len(number)):
                if guess[i] == number[i]:
                    clue.append("hot")
                elif guess[i] in number:
                    clue.append("warm")
                else:
                    clue.append("cold")
            if "hot" in clue or "warm" in clue:
                for word in clue:
                    if word == "cold":
                        clue.remove(word)
                print(" ".join(sorted(clue)))
                life -= 1
            else:
                print("cold")
                life -= 1
    won = 1
    lose = print_endgame("lose.txt")
    return lose, won


def boss_fight():
    start = 1
    while start == 1:
        return guess()

