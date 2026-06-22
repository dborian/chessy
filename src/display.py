# display.py

def display_pace(data):
    data.fenetre.blit(data.text.board,(0, 0))

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

def show_start_popup(screen, text_lines):
    import pygame
    font = pygame.font.Font(None, 28)
    btn_font = pygame.font.Font(None, 32)
    w, h = screen.get_size()
    btn_rect = pygame.Rect(0, 0, 160, 55)
    btn_rect.center = (w // 2, int(h * 0.8))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_ESCAPE):
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_rect.collidepoint(event.pos):
                    running = False

        screen.fill((20, 20, 20))
        y = int(h * 0.2)
        for line in text_lines:
            surf = font.render(line, True, (240, 240, 240))
            rect = surf.get_rect(center=(w // 2, y))
            screen.blit(surf, rect)
            y += 34
        pygame.draw.rect(screen, (200, 200, 200), btn_rect, border_radius=10)
        ok_surf = btn_font.render("OK", True, (0, 0, 0))
        ok_rect = ok_surf.get_rect(center=btn_rect.center)
        screen.blit(ok_surf, ok_rect)

        pygame.display.flip()

    return True
