import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario

import sounddevice as sd
import numpy as np

import globals

def process_sound_info(indata, outdata, frames, time, status):
    volume_level = int(np.linalg.norm(indata)*10)
    globals.setVol(volume_level)
    print("..............." + str(globals.getVol()))

windowSize = (640,480)
def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    while not menu.start:
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    globals.init()

    with sd.Stream(callback=process_sound_info):
        while not mario.restart:
            pygame.display.set_caption("Super Mario running with {:d} FPS".format(int(clock.get_fps())))
            if mario.pause:
                mario.pauseObj.update()
            else:
                level.drawLevel(mario.camera)
                dashboard.update()
                mario.update()
            pygame.display.update()
            clock.tick(max_frame_rate)
    main()


if __name__ == "__main__":
    main()
