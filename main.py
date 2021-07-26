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

# set start time
START_TIME = time.time()

class Game:
    def __init__(self):
        # create window surface
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # ...(to be done)

        # set time font
        self.font = pygame.font.SysFont("simhei", 24)

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

            self.game_time = int(time.time() - START_TIME)

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
            pygame.draw.rect(background_image, BLACK, [0, 570, 60, 30])
            minute = self.game_time // 60
            second = str(self.game_time % 60).zfill(2)
            time_text = self.font.render(f"{minute}:{second}", True, WHITE, BLACK)
            time_rect = time_text.get_rect()
            time_rect.center = (30, WIN_HEIGHT - 15)
            self.win.blit(time_text, time_rect)
            # ...(to be done)

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()

# stop initialize all the pygame module
pygame.quit()


