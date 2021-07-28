import pygame
import os

pygame.init()
BACKGROUND_IMAGE = pygame.image.load(os.path.join("images", "Map.png"))
win = pygame.display.set_mode((1024, 600))
clock = pygame.time.Clock()
points = []
# coordinate of the rect surface
run = True
while run:
    clock.tick(60)
    bg_image = pygame.transform.scale(BACKGROUND_IMAGE, (1024, 600))
    win.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            points.append((x, y))

    # draw window
    win.fill((0, 0, 0))
    # draw point
    for p in points:
        pygame.draw.circle(win, (255, 0, 0), p, 5)
    pygame.display.update()
pygame.quit()

with open('path_point.txt', 'w') as f:
    f.write(f"{points}")
