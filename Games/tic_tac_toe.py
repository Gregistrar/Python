import pandas as pd
import numpy as np
import pygame as pg
import sys
import time
from pygame.locals import *

board_dict = {'7': ' ', '8': ' ', '9': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '1': ' ', '2': ' ', '3': ' '}


def print_board(board):
    spacer = '-+-+-'
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print(spacer)
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print(spacer)
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def row_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
        if win:
            return win
    return win


def column_win(board, player):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
        if win:
            return win
    return win


def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win


def gameplay():
    turn = 'X'
    count = 1
    print_board(board_dict)
    for i in range(10):
        print("Player 1 it's your turn to move, turn {}.".format(count))
        print("Where do you want to move?")

        move = input()

        if board_dict[move] == ' ':
            board_dict[move] = turn
            count += 1
        else:
            print("That space is already taken.")
            continue

        print_board(board_dict)
        board_array = np.array([list(board_dict.values())[0:3],
                                list(board_dict.values())[3:6],
                                list(board_dict.values())[6:9]])

        row_winner = row_win(board_array, turn)
        col_winner = column_win(board_array, turn)
        diag_winner = diag_win(board_array, turn)

        if row_winner or col_winner or diag_winner:
            print("Player '{}' is the winner!".format(turn))
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


gameplay()


"""
Pygame first attempt
"""












