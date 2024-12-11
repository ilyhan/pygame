import pygame
from Render import Render

# Параметры экрана
WIDTH, HEIGHT = 800, 600

# Стилевые константы
button_border_radius = 10
circle_border_radius = 100

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 155, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Лого
logo = pygame.image.load(r'assets\images\icons\logo.svg')

# Картинки 
sound_icon_on = pygame.image.load(r"assets\images\sound-on.png")
sound_icon_off = pygame.image.load(r"assets\images\sound-off.png")
sound_icon_on_off = pygame.image.load(r"assets\images\sound-on-off.png")
back_icon = pygame.image.load(r"assets\images\back.png")
background_level = pygame.image.load(r"assets\images\background-level.jpg")
background_rule = pygame.image.load(r"assets\images\background-rule.png")
background_start = Render.load_gif(r"assets\images\background-start.png")
background_traffic = Render.load_gif(r"assets\images\background-traffic.png")
background_boom = Render.load_gif(r"assets\images\background-boom.gif")
frame_start_index = frame_traffic_index = 0
frame_start_count = len(background_start)
frame_traffic_count = len(background_traffic)
frame_boom_index = 0
frame_boom_count = len(background_boom)
explosion_active = False
explosion_pos = (0, 0)

player_car = pygame.image.load(r"assets\images\meteors\player.png")

# FPS
clock = pygame.time.Clock()
FPS = 60

# Размеры и скорость самолета и метеоритов
PLAYER_SIZE = (70, 70)
ENEMY_SIZE = (60, 60)
enemy_speed = {"Легкий": 5, "Средний": 8, "Сложный": 12}

# Игрок
player = pygame.Rect(WIDTH // 2, HEIGHT - 150, * PLAYER_SIZE)

enemy_burans = [
    pygame.image.load(r"assets\images\meteors\meteor-1.png"),
    pygame.image.load(r"assets\images\meteors\meteor-2.png"),
    pygame.image.load(r"assets\images\meteors\meteor-3.png"),
    pygame.image.load(r"assets\images\meteors\meteor-4.png"),
    pygame.image.load(r"assets\images\meteors\meteor-5.png"),
    pygame.image.load(r"assets\images\meteors\meteor-6.png"),
    pygame.image.load(r"assets\images\meteors\meteor-7.png"),
    pygame.image.load(r"assets\images\meteors\meteor-8.png"),
    pygame.image.load(r"assets\images\meteors\meteor-9.png"),
    pygame.image.load(r"assets\images\meteors\meteor-10.png"),
]