import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 50
running = True

while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), (x, 250, 20, 100))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        x += 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
