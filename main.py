import pygame, random
from utils import load_image
from pipes import make_pipes

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
Bird = pygame.transform.scale(bird1, (72, 48))
Pipe = load_image("pipe.png")

def game_over():
    wait = None
    render = font.render("Game Over", True, (255, 255, 255))
    win.blit(render, ((win.get_width() // 2) - (render.get_width() // 2), 50))
    vel = 0
    while True:
        if wait is None:
            wait = pygame.time.get_ticks()
        if (pygame.time.get_ticks() - wait) > 5000:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
    main()

def generate_pipes():
    pipe_height = random.randint(200, 400)
    pipe_height2 = random.randint(200, 400)  # Randomize the height of the second pipe
    pipe_diff = random.randint(50, 150)  # Randomize the gap between pipes
    pipe_x = 500
    pipe_x2 = pipe_x + 200
    return pipe_x, pipe_x2, pipe_height, pipe_height2

def main():
    running = True
    Bird_y = 100
    started = False
    clock = pygame.time.Clock()
    increase = False
    vel = 1
    wait = None

    pipe_x, pipe_x2, pipe_height, pipe_height2 = generate_pipes()

    while running:
        bird_rect = pygame.Rect(100, Bird_y, Bird.get_width(), Bird.get_height())
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

        if Bird_y <= 10:
            Bird_y = 10


        if Bird_y >= 600:
            render = font.render("Game Over", True, (255, 255, 255))
            win.blit(render, ((win.get_width()//2)-(render.get_width()//2), 50))
            vel = 0
            if wait is None:
                wait = pygame.time.get_ticks()

        if wait is not None and (pygame.time.get_ticks() - wait) > 5000:
            main()

        if started:
            gap = 200  # You can adjust this value or make it random
            pipe_x, pipe_x2 = make_pipes(win, Pipe, Pipe, pipe_x, pipe_x2, gap)
            pipe_x -= 5
            pipe_x2 -= 5

            if pipe_x < -Pipe.get_width():
                pipe_x, _, pipe_height, _ = generate_pipes()
            if pipe_x2 < -Pipe.get_width():
                _, pipe_x2, _, pipe_height2 = generate_pipes()

            bird_rect = pygame.Rect(100, Bird_y, Bird.get_width(), Bird.get_height())
            pipe_rect_top = pygame.Rect(pipe_x, 0, Pipe.get_width(), pipe_height)
            pipe_rect_bottom = pygame.Rect(pipe_x, pipe_height + gap, Pipe.get_width(),
                                           win.get_height() - pipe_height - gap)

            if abs(100 - pipe_x) < Bird.get_width() + Pipe.get_width():
                if bird_rect.colliderect(pipe_rect_bottom):
                    game_over()

            pipe_rect_top2 = pygame.Rect(pipe_x2, 0, Pipe.get_width(), pipe_height2)
            pipe_rect_bottom2 = pygame.Rect(pipe_x2, pipe_height2 + gap, Pipe.get_width(),
                                            win.get_height() - pipe_height2 - gap)

            if abs(100 - pipe_x2) < Bird.get_width() + Pipe.get_width():
                if bird_rect.colliderect(pipe_rect_top2) or bird_rect.colliderect(pipe_rect_bottom2):
                    game_over()

            Bird_y += vel
            vel += 1
        elif not started:
            render = font.render("Press SPACE to start", True, (255, 255, 255))
            win.blit(render, ((win.get_width()//2)-(render.get_width()//2), 50))
        pygame.display.update()

def game_over():
    render = font.render("Game Over", True, (255, 255, 255))
    win.blit(render, ((win.get_width()//2)-(render.get_width()//2), 50))
    pygame.display.update()
    pygame.time.wait(2000)
    main()

if __name__ == "__main__":
    main()