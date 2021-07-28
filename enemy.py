import pygame
import math
import os
from settings import PATH1
from settings import PATH2
from settings import RED
from settings import GREEN

pygame.init()
ENEMY_IMAGE = pygame.image.load(os.path.join("images", "enemy.png"))


class Enemy:
    def __init__(self, path_num):
        self.width = 40
        self.height = 50
        self.image = pygame.transform.scale(ENEMY_IMAGE, (self.width, self.height))
        self.health = 5
        self.max_health = 10
        # Enemy get path_num to change wave 1 and 2
        self.path_num = int(path_num)
        if self.path_num == 0:
            self.path = PATH1
        else:
            self.path = PATH2
        self.path_pos = 0
        self.move_count = 0
        self.stride = 1
        self.x, self.y = self.path[0]

    def draw(self, win):
        # draw enemy
        win.blit(self.image, (self.x - self.width // 2, self.y - self.height // 2))
        # draw enemy health bar
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        # draw enemy instant health
        pygame.draw.rect(win, RED, [self.x - 20, self.y - 40, self.max_health * 4, 5])
        pygame.draw.rect(win, GREEN, [self.x - 20, self.y - 40, self.health * 4, 5])
        # ...(to be done)

    def move(self):
        """
        stride: the length of a move
        ax, ay: 'a' means point a which is on behalf of PRESENT point
                'x', 'y' represent the x and y axis
        bx, by: 'b' means point b which is on behalf of NEXT point
                'x', 'y' represent the x and y axis
        distance_ab: distance between point a and b
        self.move_count: a counter counts steps in a move from point a to b
        max_count: get the total steps from point a to b

        unit_vector_x: unit vector of x
        unit_vector_y: unit vector of y
        delta_x: the difference in x direction
        delta_y: the difference in y direction

        main idea:
        There are many points in the PATH list;
        consequently, we should move the enemy via following those positions.
        By using if-else statement to count whether we arrive at point b from point a,
        then we move on to point c, d, e, etc, when we reach point b.
        :return: None
        """
        stride = 1
        # x, y position of point (a) on behalf of PRESENT point
        ax, ay = self.path[self.path_pos]
        # x, y position of point (b) on behalf of NEXT point
        bx, by = self.path[self.path_pos + 1]
        distance_ab = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
        max_count = int(distance_ab / stride)  # total footsteps that needed from A to B

        if self.move_count < max_count:
            unit_vector_x = (bx - ax) / distance_ab
            unit_vector_y = (by - ay) / distance_ab
            delta_x = unit_vector_x * stride
            delta_y = unit_vector_y * stride

            # update the coordinate and the counter
            self.x += delta_x
            self.y += delta_y
            self.move_count += 1
        else:
            self.path_pos += 1
            self.move_count = 0


class EnemyGroup:
    def __init__(self):
        self.gen_count = 0
        self.gen_period = 120   # (unit: frame)
        # a wave_counter is used to count whether next wave is from left or right
        self.wave_counter = 0
        self.reserved_members = []
        self.expedition = []

    def campaign(self):
        """
        main idea:
        reserve_members[]: a list is used to store enemies in one wave
        expedition[]: show enemies on the window
        first put enemy into reserve_members
        then pop out an enemy to expedition

        if-else condition, via using gen_count,
        allows enemies campaign in sequence in a round
        :return: None
        """
        if self.gen_count >= self.gen_period and not self.is_empty():
            self.expedition.append(self.reserved_members.pop())
            self.gen_count = 0
        else:
            self.gen_count += 1

    def generate(self, num):
        """
        main idea:
        by using a for loop to append a enemy into reserved_members.
        In addition, also alternate path_num via using wave_counter
        :return: None
        """
        for i in range(num):
            self.reserved_members.append(Enemy(self.wave_counter % 2))
        # ...(to be done)
        if self.wave_counter >= 1:
            self.wave_counter = 0
        else:
            self.wave_counter += 1

    def get(self):
        """
        Get the enemy list
        """
        return self.expedition

    def is_empty(self):
        """
        Return whether the enemy is empty (so that we can move on to next wave)
        """
        return False if self.reserved_members else True

    def retreat(self, enemy):
        """
        Remove the enemy from the expedition
        :param enemy: class Enemy()
        :return: None
        """
        self.expedition.remove(enemy)
