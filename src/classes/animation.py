import pygame as pg

class Animation(pg.sprite.Sprite):
    def __init__(self, image, no_frames, cooldown):
        self.sheet = pg.image.load(image).convert_alpha()
        self.no_frames = no_frames
        self.frame_list = []
        self.cooldown = cooldown

    def get_frame(self, curr_frame, width, height, rs_width, rs_height, color):
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((width * curr_frame), 0, width, height))
        image = pg.transform.scale(image, (width * rs_width, height * rs_height)) # Scale the image to the desired size
        image.set_colorkey(color) # Set the color key to black (0, 0, 0) for transparency

        return image



        