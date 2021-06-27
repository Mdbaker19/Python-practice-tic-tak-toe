import itertools
from colorama import Fore, Back, Style, init
init()

def win():

    def all_same(tic):
        if tic.count(tic[0]) == len(tic) and tic[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally -")
            return True

    # vertical wins
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically |")
            return True

    # diagonal wins
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally /")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally \\")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, display=False):
    try:
        if game_map[row][column] != 0:
            print("Spot taken. choose again")
            return game_map, False
        if not display:
            game_map[row][column] = player
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.BLUE + " O " + Style.RESET_ALL
            print(count, colored_row)
        print()
        return game_map, True

    except IndexError as e:
        print("Error! ", e)
        return game_map, False

    except Exception as e:
        print("Something went wrong!", e)
        return game_map, False


# iterable : a thing we can iterate over x = [1, 2, 3, 4] for i in x: ...
# iterator: a special object with next() method
# n = itertools.cycle(x) next(n)...next(n) and for i in n: ... infinite cycle
# y = iter(x) iterator and iterable any next call on it will pass it so next(y) then into a for loop
# the first ele is not in loop

play = True
players = [1, 2]
while play:
    game_size = int(input("What size game of tic tac toe?"))
    game = [[0 for r in range(game_size)] for c in range(game_size)]

    game_won = False
    game, _ = game_board(game, 0, 0, 0, True)
    player_choice = itertools.cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player : {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        game_won = win()
    again = input("Would you like to play again? (y / n)")
    if again.lower() == "y":
        print("restarting game...")
    elif again.lower() == "n":
        play = False
        print("have a good one")
    else:
        print("Not valid. Goodbye")
        play = False
