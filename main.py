import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
ENM_WIDTH = 60
ENM_HEIGHT = 60
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()

# create window surface
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (ENM_WIDTH, ENM_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
hp_grey_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
# ...(to be done)

# set the title
pygame.display.set_caption("My first game")
# ... (to be done)


class Game:
    def __init__(self):
        # window
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # ...(to be done)

        # set font and time
        self.font = pygame.font.SysFont("simhei", 24)
        self.text = time.time()

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True

        # clock
        clock = pygame.time.Clock()

        while run:

            # clock tick
            clock.tick(FPS)

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            # ... (to be done)

            # draw background
            self.win.blit(background_image, (0, 0))
            # ...(to be done)

            # draw enemy and health bar
            self.win.blit(enemy_image, (10, 250))
            pygame.draw.rect(background_image, (255, 0, 0), [15, 230, 50, 5])
            # ...(to be done)

            # draw menu (and buttons)
            pygame.draw.rect(background_image, (0, 0, 0), [0, 0, 1024, 80])
            self.win.blit(hp_image, (390, 0))
            self.win.blit(hp_image, (430, 0))
            self.win.blit(hp_image, (470, 0))
            self.win.blit(hp_image, (510, 0))
            self.win.blit(hp_image, (550, 0))
            self.win.blit(hp_image, (390, 40))
            self.win.blit(hp_image, (430, 40))
            self.win.blit(hp_grey_image, (470, 40))
            self.win.blit(hp_grey_image, (510, 40))
            self.win.blit(hp_grey_image, (550, 40))
            self.win.blit(muse_image, (700, 0))
            self.win.blit(sound_image, (780, 0))
            self.win.blit(continue_image, (860, 0))
            self.win.blit(pause_image, (940, 0))
            # (... to be done)

            # draw time
            text_surface = self.font.render(self.text, True, (0, 0, 255), (255, 255, 255))
            self.win.blit(text_surface, (0, 550))
            # ...(to be done)

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()

# uninitialize all the pygame module
pygame.quit()


