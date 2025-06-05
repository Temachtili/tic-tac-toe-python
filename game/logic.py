def player_win(board, player):
    # Row win
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Column win
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonal win
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_impossible(board, x_wins, o_wins):
    num_x = sum(row.count("X") for row in board)
    num_o = sum(row.count("O") for row in board)
    if abs(num_x - num_o) > 1 or (x_wins and o_wins):
        print("Impossible")
        return True
    return False


def game_is_finished(board):
    x_wins = player_win(board, "X")
    o_wins = player_win(board, "O")
    blanks = sum(row.count("_") for row in board)

    if is_impossible(board, x_wins, o_wins): pass
    if not x_wins and not o_wins:
        if blanks == 0:
            print("Draw")
        else:
            return False
    if x_wins:
        print("X wins")
    if o_wins:
        print("O wins")
    return True