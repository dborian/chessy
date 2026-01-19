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
        self.whitepace = None
        self.greypace = None
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
    x = 0
    y = 0
    b = 0
    while y != 9:
        if b == 0:
            data.fenetre.blit(data.text.whitepace,(x*130,y*130))
            b = 1
        else:
            data.fenetre.blit(data.text.greypace,(x*130,y*130))
            b = 0
        x = x + 1
        if x == 9:
            x = 0
            y = y + 1

def has_upper(s):
    return any(c.isupper() for c in s)

def display_piece(data):
    data.fenetre.blit(data.text.greenpace,(data.xp*130, data.yp*130))
    for row in range(8):
        for col in range(8):
            if data.board2[row][col] == "0" and row == data.yp and col == data.xp:
                data.fenetre.blit(data.text.orangepace,(col*130,row*130))
            elif data.board2[row][col] == "0":
                data.fenetre.blit(data.text.redpace,(col*130,row*130))
            if data.board[row][col] == "re":
                data.fenetre.blit(data.text.white.re,(col*130,row*130))
            elif data.board[row][col] == "ro":
                data.fenetre.blit(data.text.white.ro,(col*130,row*130))
            elif data.board[row][col] == "fo":
                data.fenetre.blit(data.text.white.fo,(col*130,row*130))
            elif data.board[row][col] == "ca":
                data.fenetre.blit(data.text.white.ca,(col*130,row*130))
            elif data.board[row][col] == "to":
                data.fenetre.blit(data.text.white.to,(col*130,row*130))
            elif data.board[row][col] == "pi":
                data.fenetre.blit(data.text.white.pi,(col*130,row*130))
            elif data.board[row][col] == "RE":
                data.fenetre.blit(data.text.black.re,(col*130,row*130))
            elif data.board[row][col] == "RO":
                data.fenetre.blit(data.text.black.ro,(col*130,row*130))
            elif data.board[row][col] == "FO":
                data.fenetre.blit(data.text.black.fo,(col*130,row*130))
            elif data.board[row][col] == "CA":
                data.fenetre.blit(data.text.black.ca,(col*130,row*130))
            elif data.board[row][col] == "TO":
                data.fenetre.blit(data.text.black.to,(col*130,row*130))
            elif data.board[row][col] == "PI":
                data.fenetre.blit(data.text.black.pi,(col*130,row*130))


def init_text():
    text = texture()
    text.whitepace = pygame.image.load(resource_path("text/pace/whitepace.png")).convert()
    text.greypace = pygame.image.load(resource_path("text/pace/greypace.png")).convert()
    text.greenpace = pygame.image.load(resource_path("text/pace/greenpace.png")).convert()
    text.redpace = pygame.image.load(resource_path("text/pace/redpace.png")).convert()
    text.orangepace = pygame.image.load(resource_path("text/pace/orangepace.png")).convert()
    text.white.re = pygame.image.load(resource_path("text/white/re.png")).convert_alpha()
    text.white.ro = pygame.image.load(resource_path("text/white/ro.png")).convert_alpha()
    text.white.to = pygame.image.load(resource_path("text/white/to.png")).convert_alpha()
    text.white.fo = pygame.image.load(resource_path("text/white/fo.png")).convert_alpha()
    text.white.ca = pygame.image.load(resource_path("text/white/ca.png")).convert_alpha()
    text.white.pi = pygame.image.load(resource_path("text/white/pi.png")).convert_alpha()
    text.black.re = pygame.image.load(resource_path("text/black/re.png")).convert_alpha()
    text.black.ro = pygame.image.load(resource_path("text/black/ro.png")).convert_alpha()
    text.black.to = pygame.image.load(resource_path("text/black/to.png")).convert_alpha()
    text.black.fo = pygame.image.load(resource_path("text/black/fo.png")).convert_alpha()
    text.black.ca = pygame.image.load(resource_path("text/black/ca.png")).convert_alpha()
    text.black.pi = pygame.image.load(resource_path("text/black/pi.png")).convert_alpha()
    return text

def init():
    data = info()
    data.fenetre = pygame.display.set_mode((1040, 1040))
    data.board = [
        ["to","ca","fo","re","ro","fo","ca","to"],
        ["pi","pi","pi","pi","pi","pi","pi","pi"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        ["PI","PI","PI","PI","PI","PI","PI","PI"],
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

def move_pi(data):
    if data.xp != 8 and has_upper(data.board[data.yp+1][data.xp+1]) == True:
        data.board2[data.yp+1][data.xp+1] = "0"
    if data.xp != 0 and has_upper(data.board[data.yp+1][data.xp-1]) == True:
        data.board2[data.yp+1][data.xp-1] = "0"
    if data.board[data.yp+1][data.xp] == ".":
        data.board2[data.yp+1][data.xp] = "0"
    if data.yp == 1 and data.board2[data.yp+1][data.xp] == "0" and data.board[data.yp+2][data.xp] == ".":
        data.board2[data.yp+2][data.xp] = "0"

def move_PI(data):
    if data.xp != 8 and has_upper(data.board[data.yp-1][data.xp+1]) == False and data.board[data.yp-1][data.xp+1] != ".":
        data.board2[data.yp-1][data.xp+1] = "0"
    if data.xp != 0 and has_upper(data.board[data.yp-1][data.xp-1]) == False and data.board[data.yp-1][data.xp-1] != ".":
        data.board2[data.yp-1][data.xp-1] = "0"
    if data.board[data.yp-1][data.xp] == ".":
        data.board2[data.yp-1][data.xp] = "0"
    if data.yp == 6 and data.board2[data.yp-1][data.xp] == "0" and data.board[data.yp-2][data.xp] == ".":
        data.board2[data.yp-2][data.xp] = "0"
    
def search_move(data):
    # if data.board[data.yp][data.xp] == "re":
    #     move_re(data)
    # elif data.board[data.yp][data.xp] == "ro":
    #     move_ro(data)
    # elif data.board[data.yp][data.xp] == "fo":
    #     move_fo(data)
    # elif data.board[data.yp][data.xp] == "ca":
    #     move_ca(data)
    if data.board[data.yp][data.xp] == "to":
        move_to(data)
    elif data.board[data.yp][data.xp] == "pi":
        move_pi(data)
    # elif data.board[data.yp][data.xp] == "RE":
    #     move_re(data)
    # elif data.board[data.yp][data.xp] == "RO":
    #     move_ro(data)
    # elif data.board[data.yp][data.xp] == "FO":
    #     move_fo(data)
    # elif data.board[data.yp][data.xp] == "CA":
    #     move_ca(data)
    elif data.board[data.yp][data.xp] == "TO":
        move_to(data)
    elif data.board[data.yp][data.xp] == "PI":
        move_PI(data)

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
    data = init()
    temp = [-1, -1]
    t = "."
    continuer = True
    while continuer :
        display_pace(data)
        display_piece(data)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if temp[0] == -1 and data.board[data.yp][data.xp] != ".":
                        temp[0] = data.xp
                        temp[1] = data.yp
                        t = data.board[data.yp][data.xp]
                        clear_board(data)
                        search_move(data)
                        if ft_invalid(data) == 0:
                            t = "."
                            temp[0] = -1
                            temp[1] = -1
                            clear_board(data)
                    elif temp[0] != -1:
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
                        clear_board(data)
                elif event.key == K_LEFT and data.xp != 0:
                    data.xp = data.xp - 1
                elif event.key == K_RIGHT and data.xp != 8:
                    data.xp = data.xp + 1
                elif event.key == K_UP and data.yp != 0:
                    data.yp = data.yp - 1
                elif event.key == K_DOWN and data.yp != 8:
                    data.yp = data.yp + 1
            if event.type == QUIT:
                continuer = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()