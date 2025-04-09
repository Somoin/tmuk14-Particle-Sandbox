import pygame as pg


class Button:
    def __init__(self, image_file, pos_x, pos_y, image_file_hover, b_width, b_height):
        self.image_default = pg.image.load(image_file).convert_alpha() #The original image
        self.image_hover = pg.image.load(image_file_hover).convert_alpha() #The image when hovered
        self.rect = self.image_default.get_rect(center = (pos_x, pos_y))
        self.rect.width = b_width
        self.rect.height = b_height

    def check_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False
    
    def draw(self, window):
        
        # Scale factor for the button size
        scale_factor = 1.05 
        # Check if the mouse is hovering over the button
        if self.check_hover(pg.mouse.get_pos()):
            # Transform the size of button and change image
            self.image = pg.transform.scale(self.image_hover, (self.rect.width * scale_factor, self.rect.height * scale_factor))

            # Center the button
            new_x = self.rect.centerx - (self.rect.width * scale_factor) // 2 
            new_y = self.rect.centery - (self.rect.height * scale_factor) // 2

            new_rect = pg.Rect(new_x, new_y, self.rect.width * scale_factor, self.rect.height * scale_factor)

        else:
            # Return to the original state of the button
            self.image = pg.transform.scale(self.image_default, (self.rect.width, self.rect.height))
            new_rect = self.rect
        window.blit(self.image, new_rect)
     
    def check_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False
        
