import pygame as pg

class TextDisplay:
    def __init__(self, window, text, pos_x, pos_y, color):
        self.window = window
        self.text = text
        self.font = pg.font.Font(None, 30) # Default font to match the fps counter
        self.color = color
        self.display_text = self.font.render(self.text, True, self.color)
        self.display_text_rect = self.display_text.get_rect(topleft=(pos_x, pos_y))

    def draw(self):
        self.display_text = self.font.render(self.text, True, self.color)
        self.window.blit(self.display_text, self.display_text_rect)