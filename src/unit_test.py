import pytest
import pygame as pg
from main import ParticleType
from configparser import ConfigParser

from classes.button import Button


pg.init()
config_object = ConfigParser()

config_object.read("config.ini")
cell_size = config_object.getint("CONFIG", "cell_size")
window_width = config_object.getint("CONFIG", "window_width")
window_height = config_object.getint("CONFIG", "window_height")
FPS = config_object.getint("CONFIG", "FPS")
window = pg.display.set_mode((window_width, window_height))

pg.display.set_caption("Particle Sandbox")


def button_check_hover(x):
    button = Button("images/sandbutton.png", 0, 0, "images/sandbutton_hover.png", 100, 100)
    return button.check_hover((x, x))

def button_check_press(x, particle_type):
    button = Button("images/waterbutton.png", 0, 0, "images/waterbutton_hover.png", 100, 100)
    if button.check_press((x, x)):
        return True if particle_type == ParticleType.WATER else False
           

def test_answer():
    assert button_check_hover(10) == True
    assert button_check_press(10, ParticleType.WATER) == True
