from pico2d import *
import game_world
import game_framework
import random

#Bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # km/hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = 800, 400
        self.frame = 0
        self.face_dir = 1

    def draw(self):
        # if self.face_dir == -1:
        #     Bird.image.clip_composite_draw(int(self.frame) * 183, (2-(int(self.frame)//5)) * 168,
        #                                    168, 183, 0, 'h', self.x, self.y, 100, 100)
        # else:
        Bird.image.clip_draw((int(self.frame))%5 * 183, (2-(int(self.frame)//5)) * 168, 183, 168, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        pass