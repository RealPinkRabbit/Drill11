from pico2d import *
import game_world
import random

class Bird:
    image = None

    def __init__(self):
        if Bird.iamge == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = 800, 400
        self.frame = 0