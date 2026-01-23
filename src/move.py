# move.py
from utils import has_upper, clear_board

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