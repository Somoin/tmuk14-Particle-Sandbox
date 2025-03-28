import pygame as pg


class Button:
    def __init__(self, image_file, pos_x, pos_y, image_file_hover):
        self.image = pg.image.load(image_file).convert_alpha()
        self.image_hover = pg.image.load(image_file_hover).convert_alpha()
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

    def check_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            False
    
    def draw(self, window):
        # Check if the mouse is hovering over the button
        if self.check_hover(pg.mouse.get_pos()):
            # Transform the size of button
            self.image = pg.transform.scale(self.image_hover, (self.rect.width+5, self.rect.height+5))
        else:
            self.image = pg.transform.scale(self.image, (self.rect.width, self.rect.height))
        window.blit(self.image, self.rect)
     
    def check_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False