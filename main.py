import pygame, random
from utils import load_image

pygame.init()

win = pygame.display.set_mode((500, 600))

pygame.display.set_caption("Flappy Bird")
pygame.font.init()
font = pygame.font.SysFont("comicsans", 30)

Bird = load_image("bird.png")
bird1 = pygame.surface.Surface((18, 12))
bird1.fill((0, 0, 0))
bird1.blit(Bird, (0, 0))
bird1.set_colorkey((0, 0, 0))
Bird = pygame.transform.scale(bird1, (72,48))
Pipe = load_image("pipe.png")

def main():
    running = True
    Bird_y = 100
    started = False
    clock = pygame.time.Clock()
    increase = False
    vel = 1
    wait = None

    while running:
        win.fill((120, 180, 255))
        win.blit(Bird, (100, Bird_y))
        clock.tick(30)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            started = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    increase = True

        if increase and vel > -40:
            vel -= 10
        if increase and vel <= 0:
            increase = False

        if Bird_y >= 600:
            render = font.render("Game Over", True, (255, 255, 255))
            win.blit(render, ((win.get_width()//2)-(render.get_width()//2), 50))
            vel = 0
            if wait is None:
                wait = pygame.time.get_ticks()

        if wait is not None and (pygame.time.get_ticks() - wait) > 5000:
            main()


        if started:
            Bird_y += vel
            vel += 1
        elif not started:
            render = font.render("Press SPACE to start", True, (255, 255, 255))
            win.blit(render, ((win.get_width()//2)-(render.get_width()//2), 50))
        pygame.display.update()

if __name__ == "__main__":
    main()
