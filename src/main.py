import pygame
from pygame.locals import *
import sys
import os
from move import *
from utils import debug, has_upper, ft_invalid
from display import display_pace, display_piece, show_start_popup
from init_game import init

def ft_whatdowedo(data, p):
    xp = 0
    yp = 0
    temp =  [-1, -1]
    w, h = data.fenetre.get_size()
    y = int(h * 0.2)
    font = pygame.font.Font(None, 28)
    if p == 0:
            xp = data.xp
            yp = data.yp
            for row in range(8):
                if p == 2:
                    p = 0
                    return temp
                for col in range(8):
                    if data.board[row][col] == "ro":
                        print("test")
                        data.xp = col
                        data.yp = row
                        if is_ok(row, col, data) == False:
                            print("ntm la pute")
                            temp[0] = col
                            temp[1] = row
                            t = data.board[row][col]
                            data.xp == col
                            data.yp == row
                            search_move(data, 0)
                            if ft_invalid(data) == 0:
                                surf = font.render("white lose", True, (255, 0, 0))
                                rect = surf.get_rect(center=(w // 2, y))
                                data.fenetre.blit(surf, rect)
                                exit
                            p = 2
                            return temp
                        else:
                            p = 2
                            data.xp = xp
                            data.yp = yp
                            return temp
    return temp

def main():
    pygame.init()
    pygame.display.set_caption("Chessy")
    data = init()
    temp = [-1, -1]
    t = "."
    continuer = True
    p = 0
    while continuer :
        display_pace(data)
        display_piece(data)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if (temp[0] == -1 and data.board[data.yp][data.xp] != ".") and ((p == 0 and has_upper(data.board[data.yp][data.xp]) == False) or (p == 1 and has_upper(data.board[data.yp][data.xp]) == True)):
                        temp[0] = data.xp
                        temp[1] = data.yp
                        clear_board(data)
                        search_move(data, 0)
                        if ft_invalid(data) == 0:
                            temp[0] = -1
                            temp[1] = -1
                            clear_board(data)
                    elif temp[0] != -1:
                        if data.yp == temp[1] and data.xp == temp[0]:
                            temp[0] = -1
                            temp[1] = -1
                            clear_board(data)
                            continue
                        if data.board2[data.yp][data.xp] != "0":
                            continue
                        t = data.board[temp[1]][temp[0]]
                        if has_upper(t) == False and has_upper(data.board[data.yp][data.xp]) == True:
                            data.board[temp[1]][temp[0]] = "."
                        elif has_upper(t) == True and has_upper(data.board[data.yp][data.xp]) == False:
                            data.board[temp[1]][temp[0]] = "."
                        else:
                            data.board[temp[1]][temp[0]] = data.board[data.yp][data.xp]    
                        data.board[data.yp][data.xp] = t
                        temp[0] = -1
                        temp[1] = -1
                        if p == 0:
                            p = 1
                        else:
                            p = 0
                        clear_board(data)
                        temp = ft_whatdowedo(data, p)
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
