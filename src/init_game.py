# start.py
import pygame
from pygame.locals import *
from display import show_start_popup
from utils import resource_path
from class_game import info, texture

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
    text_lines = [
    "Game code licensed under the GNU GPLv3.",
    "Any redistributed version must keep the source code public.",
    "",
    "Chess art by Joszs",
    "Licensed under CC BY 4.0",
    "Source: joszs.itch.io"
    ]
    show_start_popup(data.fenetre, text_lines)
    data.text = init_text()
    return data