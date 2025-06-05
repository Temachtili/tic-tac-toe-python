# tests/test_logic.py
import pytest
from game.logic import player_win, is_impossible, game_is_finished

def test_win_row():
    board = [
        ["X", "X", "X"],
        ["_", "O", "_"],
        ["_", "_", "O"]
    ]
    assert player_win(board, "X") is True
    assert player_win(board, "O") is False

def test_win_column():
    board = [
        ["X", "O", "_"],
        ["X", "O", "_"],
        ["X", "_", "_"]
    ]
    assert player_win(board, "X") is True
    assert player_win(board, "O") is False

def test_diagonal_win():
    board = [
        ["X", "_", "O"],
        ["_", "X", "_"],
        ["_", "_", "X"]
    ]
    assert player_win(board, "X") is True

def test_is_impossible_too_many_x():
    board = [
        ["X", "X", "X"],
        ["X", "O", "O"],
        ["X", "O", "X"]
    ]
    assert is_impossible(board, True, False) is True

def test_draw():
    board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]
    assert game_is_finished(board) is True
