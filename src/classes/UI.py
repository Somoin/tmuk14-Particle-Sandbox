import pygame as pg
from classes.button import Button
from classes.fps_counter import fps_counter

class UIElement:
    def __init__(self, window, pos):
        self.window = window
        self.pos = pos
    
    def render(self, window):
        pass

    def update(self, window):
        pass
       

  
class UI:
    def __init__(self, window, UIElements : list[UIElement]):
        self.UIElements = UIElements
        self.window = window

    def update_UI(self):
        for element in self.UIElements:
            element.update(self)
            element.render(self)
            

    
        
