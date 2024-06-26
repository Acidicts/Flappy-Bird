import pygame

def make_pipes(win, pipe1, pipe2, x1, x2, gap=200):
    win.blit(pygame.transform.scale(pipe1, (128,256*1.5)), (x1, (256*2)-gap))
    win.blit(pygame.transform.scale(pygame.transform.flip(pipe2, False, True), (128, 256*1.5)), (x2, 0-(gap//2)))

    return x1, x2