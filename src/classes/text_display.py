import pygame as pg
from UI import UIElement

class TextDisplay(UIElement):
    def __init__(self, window, text, pos, color):
        self.window = window
        self.text = text
        self.font = pg.font.Font(None, 30) # Default font to match the fps counter
        self.color = color
        self.display_text = self.font.render(self.text, True, self.color)
        self.display_text_rect = self.display_text.get_rect(topleft=(pos[0], pos[1]))

    def render(self):
        self.display_text = self.font.render(self.text, True, self.color)
        self.window.blit(self.display_text, self.display_text_rect)