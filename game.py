#!/usr/bin/python

import pygame
from pygame.locals import *
from settings import DISPLAY, FLAGS, DEPTH, TITLE, FPS
from scene_manager import SceneMananger

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    running = True

    manager = SceneMananger()

    while running:
        clock.tick(FPS)

        if pygame.event.get(QUIT):
            running = False
            return
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)
        pygame.display.flip()


if __name__ == "__main__": main()
