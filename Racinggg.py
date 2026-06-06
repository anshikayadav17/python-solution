import pygame

pygame.init()

screen = pygame.display.set_mode((400, 600))
car_x = 180

running = True

while running:
    screen.fill((200, 200, 200))

    pygame.draw.rect(screen, (255, 0, 0), (car_x, 500, 40, 80))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= 5
    if keys[pygame.K_RIGHT]:
        car_x += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
