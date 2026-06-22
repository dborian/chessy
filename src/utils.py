# utils.py
import os
import sys

def debug(data):
    for row in range(8):
        for col in range(8):
            print(data.board2[row][col], end=" ")
        print("")

def has_upper(s):
    return any(c.isupper() for c in s)


def ft_invalid(data):
    i = 0
    for row in range(8):
        for col in range(8):
            if data.board2[row][col] == "0":
                i += 1
    return i

def clear_board(data):
    for row in range(8):
        for col in range(8):
            if data.board2[row][col] == "0" or data.board2[row][col] == "1":
                data.board2[row][col] = "."

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)