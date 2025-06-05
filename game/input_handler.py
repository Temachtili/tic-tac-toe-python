def get_valid_coordinates(board):
    while True:
        try:
            x_cord, o_cord = map(int, input().split())
        except ValueError:
            print("You should enter numbers!")
        else:
            if not (1 <= x_cord <= 3) or not (1 <= o_cord <= 3):
                print("Coordinates should be from 1 to 3!")
            elif board[x_cord - 1][o_cord - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                return x_cord, o_cord
