import pygame
import random
from constants import *

class Burans:
    def __init__(self, enemies, player):
        self.enemy_burans = enemies
        self.player = player
        self.speed = 5
        self.enemies = []

    def spawn_enemy(self):
        x_pos = random.randint(0, WIDTH - ENEMY_SIZE[0])
        y_pos = random.randint(-HEIGHT, -ENEMY_SIZE[1])
        enemy_rect = pygame.Rect(x_pos, y_pos, *ENEMY_SIZE)

        # Проверяем, что враг не накладывается на существующие
        for existing_enemy, _ in self.enemies:
            if enemy_rect.colliderect(existing_enemy):
                return  # Враг не будет добавлен, если есть наложение

        enemy_buran = random.choice(enemy_burans)
        self.enemies.append((enemy_rect, enemy_buran))

    def player_move(self, keys):
        if keys[pygame.K_LEFT] and self.player.left > 0:
            self.player.x -= self.speed
        if keys[pygame.K_RIGHT] and self.player.right < WIDTH:
            self.player.x += self.speed
        if keys[pygame.K_UP] and self.player.top > 0:
            self.player.y -= self.speed
        if keys[pygame.K_DOWN] and self.player.bottom < HEIGHT:
            self.player.y += self.speed