from game.board import print_board
from game.logic import game_is_finished
from game.input_handler import get_valid_coordinates

def main():
    board = [["_"] * 3 for _ in range(3)]
    print_board(board)

    game_finished = False
    x_plays = True

    while not game_finished:
        x_cord, o_cord = get_valid_coordinates(board)
        board[x_cord - 1][o_cord - 1] = "X" if x_plays else "O"
        x_plays = not x_plays
        print_board(board)
        game_finished = game_is_finished(board)


main()
