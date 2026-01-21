import pygame
from pygame.locals import *
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class pion:
    def __init__(self):
        self.re = None
        self.ro = None
        self.fo = None
        self.ca = None
        self.to = None
        self.pi = None

class texture:
    def __init__(self):
        self.board = None
        self.greenpace = None
        self.orange = None
        self.redpace = None
        self.white = pion()
        self.black = pion()

class info:
    def __init__(self):
        self.board = None
        self.board2 = None
        self.fenetre = None
        self.text = texture()
        self.xp = 0
        self.yp = 0

def display_pace(data):
    data.fenetre.blit(data.text.board,(0, 0))    

def has_upper(s):
    return any(c.isupper() for c in s)

def display_piece(data):
    data.fenetre.blit(data.text.greenpace,(data.xp*128, data.yp*128))
    for row in range(8):
        for col in range(8):
            if data.board2[row][col] == "0" and row == data.yp and col == data.xp:
                data.fenetre.blit(data.text.orangepace,(col*128,row*128))
            elif data.board2[row][col] == "0":
                data.fenetre.blit(data.text.redpace,(col*128,row*128))
            if data.board[row][col] == "re":
                data.fenetre.blit(data.text.white.re,(col*128,row*128))
            elif data.board[row][col] == "ro":
                data.fenetre.blit(data.text.white.ro,(col*128,row*128))
            elif data.board[row][col] == "fo":
                data.fenetre.blit(data.text.white.fo,(col*128,row*128))
            elif data.board[row][col] == "ca":
                data.fenetre.blit(data.text.white.ca,(col*128,row*128))
            elif data.board[row][col] == "to":
                data.fenetre.blit(data.text.white.to,(col*128,row*128))
            elif data.board[row][col] == "pi":
                data.fenetre.blit(data.text.white.pi,(col*128,row*128))
            elif data.board[row][col] == "RE":
                data.fenetre.blit(data.text.black.re,(col*128,row*128))
            elif data.board[row][col] == "RO":
                data.fenetre.blit(data.text.black.ro,(col*128,row*128))
            elif data.board[row][col] == "FO":
                data.fenetre.blit(data.text.black.fo,(col*128,row*128))
            elif data.board[row][col] == "CA":
                data.fenetre.blit(data.text.black.ca,(col*128,row*128))
            elif data.board[row][col] == "TO":
                data.fenetre.blit(data.text.black.to,(col*128,row*128))
            elif data.board[row][col] == "PI":
                data.fenetre.blit(data.text.black.pi,(col*128,row*128))


def init_text():
    text = texture()
    text.board = pygame.image.load(resource_path("text/pace/board.png")).convert_alpha()
    text.board = pygame.transform.scale(text.board, (1024, 1024))
    text.greenpace = pygame.image.load(resource_path("text/pace/greenpace.png")).convert()
    text.greenpace = pygame.transform.scale(text.greenpace, (128, 128))
    text.redpace = pygame.image.load(resource_path("text/pace/redpace.png")).convert()
    text.redpace = pygame.transform.scale(text.redpace, (128, 128))
    text.orangepace = pygame.image.load(resource_path("text/pace/orangepace.png")).convert()
    text.orangepace = pygame.transform.scale(text.orangepace, (128, 128))
    text.white.re = pygame.image.load(resource_path("text/white/re.png")).convert_alpha()
    text.white.re = pygame.transform.scale(text.white.re, (128, 128))
    text.white.ro = pygame.image.load(resource_path("text/white/ro.png")).convert_alpha()
    text.white.ro = pygame.transform.scale(text.white.ro, (128, 128))
    text.white.to = pygame.image.load(resource_path("text/white/to.png")).convert_alpha()
    text.white.to = pygame.transform.scale(text.white.to, (128, 128))
    text.white.fo = pygame.image.load(resource_path("text/white/fo.png")).convert_alpha()
    text.white.fo = pygame.transform.scale(text.white.fo, (128, 128))
    text.white.ca = pygame.image.load(resource_path("text/white/ca.png")).convert_alpha()
    text.white.ca = pygame.transform.scale(text.white.ca, (128, 128))
    text.white.pi = pygame.image.load(resource_path("text/white/pi.png")).convert_alpha()
    text.white.pi = pygame.transform.scale(text.white.pi, (128, 128))
    text.black.re = pygame.image.load(resource_path("text/black/re.png")).convert_alpha()
    text.black.re = pygame.transform.scale(text.black.re, (128, 128))
    text.black.ro = pygame.image.load(resource_path("text/black/ro.png")).convert_alpha()
    text.black.ro = pygame.transform.scale(text.black.ro, (128, 128))
    text.black.to = pygame.image.load(resource_path("text/black/to.png")).convert_alpha()
    text.black.to = pygame.transform.scale(text.black.to, (128, 128))
    text.black.fo = pygame.image.load(resource_path("text/black/fo.png")).convert_alpha()
    text.black.fo = pygame.transform.scale(text.black.fo, (128, 128))
    text.black.ca = pygame.image.load(resource_path("text/black/ca.png")).convert_alpha()
    text.black.ca = pygame.transform.scale(text.black.ca, (128, 128))
    text.black.pi = pygame.image.load(resource_path("text/black/pi.png")).convert_alpha()
    text.black.pi = pygame.transform.scale(text.black.pi, (128, 128))
    return text

def init():
    data = info()
    data.fenetre = pygame.display.set_mode((1024, 1024))
    data.board = [
        ["to","ca","fo","re","ro","fo","ca","to"],
        ["pi","pi","pi","pi","pi","pi","pi","pi"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["PI","PI","PI","PI","PI","PI","PI","PI",],
        ["TO","CA","FO","RE","RO","FO","CA","TO"],
    ]
    data.board2 = [
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
    ]
    data.text = init_text()
    return data


def move_fo(data):
    x = data.xp +1
    y = data.yp +1
    while x != 8 and y != 8 and data.board[y][x] == ".":
        data.board2[y][x] = "0"
        x = x + 1
        y = y + 1
    if x != 8 and y != 8:
        if has_upper(data.board[y][x]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[y][x] = "0"
        if has_upper(data.board[y][x]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[y][x] = "0"
    x = data.xp -1
    y = data.yp +1
    while x != -1 and y != 8 and data.board[y][x] == ".":
        data.board2[y][x] = "0"
        x = x - 1
        y = y + 1
    if x != -1 and y != 8:
        if has_upper(data.board[y][x]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[y][x] = "0"
        if has_upper(data.board[y][x]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[y][x] = "0"    
    x = data.xp +1
    y = data.yp -1
    while y != -1 and x != 8 and data.board[y][x] == ".":
        data.board2[y][x] = "0"
        y = y - 1
        x = x + 1
    if y != -1 and x != 8:
        if has_upper(data.board[y][x]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[y][x] = "0"
        if has_upper(data.board[y][x]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[y][x] = "0"
    x = data.xp -1
    y = data.yp -1
    while y != -1 and x != -1 and data.board[y][x] == ".":
        data.board2[y][x] = "0"
        y = y - 1
        x = x - 1
    if y != -1 and x != - 1:
        if has_upper(data.board[y][x]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[y][x] = "0"
        if has_upper(data.board[y][x]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[y][x] = "0"

def move_to(data):
    x = data.xp +1
    y = data.yp +1
    x1 = data.xp -1
    y1 = data.yp -1
    while x != 8 and data.board[data.yp][x] == ".":
        data.board2[data.yp][x] = "0"
        x = x + 1
    if x != 8:
        if has_upper(data.board[data.yp][x]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[data.yp][x] = "0"
        if has_upper(data.board[data.yp][x]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[data.yp][x] = "0"
    while x1 != -1 and data.board[data.yp][x1] == ".":
        data.board2[data.yp][x1] = "0"
        x1 = x1 - 1
    if x1 != -1:
        if has_upper(data.board[data.yp][x1]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[data.yp][x1] = "0"
        if has_upper(data.board[data.yp][x1]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[data.yp][x1] = "0"
    while y != 8 and data.board[y][data.xp] == ".":
        data.board2[y][data.xp] = "0"
        y = y + 1
    if y != 8:
        if has_upper(data.board[y][data.xp]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[y][data.xp] = "0"
        if has_upper(data.board[y][data.xp]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[y][data.xp] = "0"
    while y1 != -1 and data.board[y1][data.xp] == ".":
        data.board2[y1][data.xp] = "0"
        y1 = y1 - 1
    if y1 != -1:
        if has_upper(data.board[y1][data.xp]) == True and has_upper(data.board[data.yp][data.xp]) == False:
            data.board2[y1][data.xp] = "0"
        if has_upper(data.board[y1][data.xp]) == False and has_upper(data.board[data.yp][data.xp]) == True:
            data.board2[y1][data.xp] = "0"

def move_pi(data, b):
    if b == 1:
        if data.xp != 7 and data.yp != 7:
            data.board2[data.yp+1][data.xp+1] = "0"
        if data.xp != 0 and data.yp != 7:
            data.board2[data.yp+1][data.xp-1] = "0"
        return
    if data.xp != 7 and has_upper(data.board[data.yp+1][data.xp+1]) == True:
        data.board2[data.yp+1][data.xp+1] = "0"
    if data.xp != 0 and has_upper(data.board[data.yp+1][data.xp-1]) == True:
        data.board2[data.yp+1][data.xp-1] = "0"
    if b == 0:
        if data.board[data.yp+1][data.xp] == ".":
            data.board2[data.yp+1][data.xp] = "0"
        if data.yp == 1 and data.board2[data.yp+1][data.xp] == "0" and data.board[data.yp+2][data.xp] == ".":
            data.board2[data.yp+2][data.xp] = "0"

def is_ok(y, x, data):
    temp = [row[:] for row in data.board2]
    xt = data.xp
    yt = data.yp
    if has_upper(data.board[data.yp][data.xp]) == False:
        for row in range(8):
            for col in range(8):
                if has_upper(data.board[row][col]) == True and data.board[row][col] != "RO":
                    data.xp = col
                    data.yp = row
                    clear_board(data)
                    search_move(data, 1)
                    if data.board2[y][x] == "0":
                        data.board2 = temp
                        data.xp = xt
                        data.yp = yt
                        return False
    elif has_upper(data.board[data.yp][data.xp]) == True:
        for row in range(8):
            for col in range(8):
                if has_upper(data.board[row][col]) == False and data.board[row][col] != "ro":
                    data.xp = col
                    data.yp = row
                    clear_board(data)
                    search_move(data, 1)
                    if data.board2[y][x] == "0":
                        data.board2 = temp
                        data.xp = xt
                        data.yp = yt
                        return False
    data.board2 = temp
    data.xp = xt
    data.yp = yt
    return True

def move_ro(data):
    if (data.yp != 0 and is_ok(data.yp-1, data.xp, data) == True) and (data.board[data.yp-1][data.xp] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp - 1][data.xp]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp - 1][data.xp]) == True):
        data.board2[data.yp-1][data.xp] = "0"
    if (data.yp != 7 and is_ok(data.yp+1, data.xp, data) == True) and (data.board[data.yp+1][data.xp] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp + 1][data.xp]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp + 1][data.xp]) == True):
        data.board2[data.yp+1][data.xp] = "0"
    if (data.xp != 0 and is_ok(data.yp, data.xp-1, data) == True) and (data.board[data.yp][data.xp-1] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp][data.xp-1]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp][data.xp-1]) == True):
        data.board2[data.yp][data.xp-1] = "0"
    if (data.xp != 7 and is_ok(data.yp, data.xp+1, data) == True) and (data.board[data.yp][data.xp+1] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp][data.xp+1]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp][data.xp+1]) == True):
        data.board2[data.yp][data.xp+1] = "0"
    if (data.xp != 7 and data.yp != 7 and is_ok(data.yp+1, data.xp+1, data) == True) and (data.board[data.yp+1][data.xp+1] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp + 1][data.xp + 1]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp + 1][data.xp + 1]) == True):
        data.board2[data.yp+1][data.xp+1] = "0"
    if (data.xp != 0 and data.yp != 0 and is_ok(data.yp-1, data.xp-1, data) == True) and (data.board[data.yp-1][data.xp-1] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp - 1][data.xp - 1]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp - 1][data.xp - 1]) == True):
        data.board2[data.yp-1][data.xp-1] = "0"
    if (data.xp != 0 and data.yp != 7 and is_ok(data.yp+1, data.xp-1, data) == True) and (data.board[data.yp+1][data.xp-1] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp + 1][data.xp - 1]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp + 1][data.xp - 1]) == True):
        data.board2[data.yp+1][data.xp-1] = "0"
    if (data.xp != 7 and data.yp != 0 and is_ok(data.yp-1, data.xp+1, data) == True) and (data.board[data.yp-1][data.xp+1] == "." or has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp - 1][data.xp + 1]) == False or has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp - 1][data.xp + 1]) == True):
        data.board2[data.yp-1][data.xp+1] = "0"


def move_PI(data, b):
    if b == 1:
        if data.xp != 7:
            data.board2[data.yp-1][data.xp+1] = "0"
        if data.xp != 0:
            data.board2[data.yp-1][data.xp-1] = "0"
        return
    if data.xp != 7 and has_upper(data.board[data.yp-1][data.xp+1]) == False and data.board[data.yp-1][data.xp+1] != ".":
        data.board2[data.yp-1][data.xp+1] = "0"
    if data.xp != 0 and has_upper(data.board[data.yp-1][data.xp-1]) == False and data.board[data.yp-1][data.xp-1] != ".":
        data.board2[data.yp-1][data.xp-1] = "0"
    if data.board[data.yp-1][data.xp] == ".":
        data.board2[data.yp-1][data.xp] = "0"
    if data.yp == 6 and data.board2[data.yp-1][data.xp] == "0" and data.board[data.yp-2][data.xp] == ".":
        data.board2[data.yp-2][data.xp] = "0"

def move_ca(data):
    if data.yp < 6 and data.xp != 7 and data.board[data.yp + 2][data.xp + 1] == "." or data.yp < 5 and data.xp != 7 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp + 2][data.xp + 1]) == True:
        data.board2[data.yp + 2][data.xp + 1] = "0"
    if data.yp < 6 and data.xp != 0 and data.board[data.yp + 2][data.xp - 1] == "." or data.yp < 5 and data.xp != 0 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp + 2][data.xp - 1]) == True:
        data.board2[data.yp + 2][data.xp - 1] = "0"
    if data.yp != 7 and data.xp >= 2  and data.board[data.yp + 1][data.xp - 2] == "." or data.yp != 7 and data.xp > 2 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp + 1][data.xp - 2]) == True:
        data.board2[data.yp + 1][data.xp - 2] = "0"
    if data.yp != 7 and data.xp <= 5  and data.board[data.yp + 1][data.xp + 2] == "." or data.yp != 7 and data.xp <= 5 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp + 1][data.xp + 2]) == True:
        data.board2[data.yp + 1][data.xp + 2] = "0"
    if data.yp >= 2 and data.xp != 0 and data.board[data.yp - 2][data.xp - 1] == "." or data.yp >= 2 and data.xp != 0 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp - 2][data.xp - 1]) == True:
        data.board2[data.yp - 2][data.xp - 1] = "0"
    if data.yp >= 2 and data.xp != 7 and data.board[data.yp - 2][data.xp + 1] == "." or data.yp >= 2 and data.xp != 7 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp - 2][data.xp + 1]) == True:
        data.board2[data.yp - 2][data.xp + 1] = "0"
    if data.yp != 0 and data.xp >= 2  and data.board[data.yp - 1][data.xp - 2] == "." or data.yp != 0 and data.xp >= 2 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp - 1][data.xp - 2]) == True:
        data.board2[data.yp - 1][data.xp - 2] = "0"
    if data.yp != 0 and data.xp <= 5  and data.board[data.yp - 1][data.xp + 2] == "." or data.yp != 0 and data.xp <= 5 and has_upper(data.board[data.yp][data.xp]) == False and has_upper(data.board[data.yp - 1][data.xp + 2]) == True:
        data.board2[data.yp - 1][data.xp + 2] = "0"

def move_CA(data):
    if data.yp < 6 and data.xp != 7 and data.board[data.yp + 2][data.xp + 1] == "." or data.yp < 5 and data.xp != 7 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp + 2][data.xp + 1]) == False:
        data.board2[data.yp + 2][data.xp + 1] = "0"
    if data.yp < 6 and data.xp != 0 and data.board[data.yp + 2][data.xp - 1] == "." or data.yp < 5 and data.xp != 0 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp + 2][data.xp - 1]) == False:
        data.board2[data.yp + 2][data.xp - 1] = "0"
    if data.yp != 7 and data.xp >= 2  and data.board[data.yp + 1][data.xp - 2] == "." or data.yp != 7 and data.xp > 2 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp + 1][data.xp - 2]) == False:
        data.board2[data.yp + 1][data.xp - 2] = "0"
    if data.yp != 7 and data.xp <= 5  and data.board[data.yp + 1][data.xp + 2] == "." or data.yp != 7 and data.xp <= 5 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp + 1][data.xp + 2]) == False:
        data.board2[data.yp + 1][data.xp + 2] = "0"
    if data.yp >= 2 and data.xp != 0 and data.board[data.yp - 2][data.xp - 1] == "." or data.yp >= 2 and data.xp != 0 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp - 2][data.xp - 1]) == False:
        data.board2[data.yp - 2][data.xp - 1] = "0"
    if data.yp >= 2 and data.xp != 7 and data.board[data.yp - 2][data.xp + 1] == "." or data.yp >= 2 and data.xp != 7 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp - 2][data.xp + 1]) == False:
        data.board2[data.yp - 2][data.xp + 1] = "0"
    if data.yp != 0 and data.xp >= 2  and data.board[data.yp - 1][data.xp - 2] == "." or data.yp != 0 and data.xp >= 2 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp - 1][data.xp - 2]) == False:
        data.board2[data.yp - 1][data.xp - 2] = "0"
    if data.yp != 0 and data.xp <= 5  and data.board[data.yp - 1][data.xp + 2] == "." or data.yp != 0 and data.xp <= 5 and has_upper(data.board[data.yp][data.xp]) == True and has_upper(data.board[data.yp - 1][data.xp + 2]) == False:
        data.board2[data.yp - 1][data.xp + 2] = "0"

def search_move(data, b):
    if data.board[data.yp][data.xp] == "re":
        move_to(data)
        move_fo(data)
    elif data.board[data.yp][data.xp] == "ro":
        move_ro(data)
    elif data.board[data.yp][data.xp] == "fo":
        move_fo(data)
    elif data.board[data.yp][data.xp] == "ca":
        move_ca(data)
    elif data.board[data.yp][data.xp] == "to":
        move_to(data)
    elif data.board[data.yp][data.xp] == "pi":
        move_pi(data, b)
    elif data.board[data.yp][data.xp] == "RE":
        move_to(data)
        move_fo(data)
    elif data.board[data.yp][data.xp] == "RO":
        move_ro(data)
    elif data.board[data.yp][data.xp] == "FO":
        move_fo(data)
    elif data.board[data.yp][data.xp] == "CA":
        move_CA(data)
    elif data.board[data.yp][data.xp] == "TO":
        move_to(data)
    elif data.board[data.yp][data.xp] == "PI":
        move_PI(data, b)
    for row in range(8):
        for col in range(8):
            if data.board[row][col] == "ro" or data.board[row][col] == "RO":
                data.board2[row][col] = "."

def clear_board(data):
    for row in range(8):
        for col in range(8):
            if data.board2[row][col] == "0" or data.board2[row][col] == "1":
                data.board2[row][col] = "."

def debug(data):
    for row in range(8):
        for col in range(8):
            print(data.board2[row][col], end=" ")
        print("")

def ft_invalid(data):
    i = 0
    for row in range(8):
        for col in range(8):
            if data.board2[row][col] == "0":
                i += 1
    return i

def main():
    pygame.init()
    pygame.display.set_caption("Chessy")
    data = init()
    temp = [-1, -1]
    t = "."
    continuer = True
    p = 1
    while continuer :
        display_pace(data)
        display_piece(data)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if (temp[0] == -1 and data.board[data.yp][data.xp] != ".") and ((p == 0 and has_upper(data.board[data.yp][data.xp]) == False) or (p == 1 and has_upper(data.board[data.yp][data.xp]) == True)):
                        temp[0] = data.xp
                        temp[1] = data.yp
                        t = data.board[data.yp][data.xp]
                        clear_board(data)
                        search_move(data, 0)
                        if ft_invalid(data) == 0:
                            t = "."
                            temp[0] = -1
                            temp[1] = -1
                            clear_board(data)
                    elif temp[0] != -1:
                        if data.yp == temp[1] and data.xp == temp[0]:
                            t = "."
                            temp[0] = -1
                            temp[1] = -1
                            clear_board(data)
                            continue
                        if data.board2[data.yp][data.xp] != "0":
                            continue
                        if has_upper(t) == False and has_upper(data.board[data.yp][data.xp]) == True:
                            data.board[temp[1]][temp[0]] = "."
                        elif has_upper(t) == True and has_upper(data.board[data.yp][data.xp]) == False:
                            data.board[temp[1]][temp[0]] = "."
                        else:
                            data.board[temp[1]][temp[0]] = data.board[data.yp][data.xp]    
                        data.board[data.yp][data.xp] = t
                        t = "."
                        temp[0] = -1
                        temp[1] = -1
                        if p == 0:
                            p = 1
                        else:
                            p = 0
                        clear_board(data)
                elif event.key == K_LEFT and data.xp != 0:
                    data.xp = data.xp - 1
                elif event.key == K_RIGHT and data.xp != 7:
                    data.xp = data.xp + 1
                elif event.key == K_UP and data.yp != 0:
                    data.yp = data.yp - 1
                elif event.key == K_DOWN and data.yp != 7:
                    data.yp = data.yp + 1
            if event.type == QUIT:
                continuer = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
