import pygame
import random
import sys

from PIL import Image
from Render import Render
from Database import Database as DB
from Sound import Sound
from constants import *
from Buran import Burans

# Инициализация pygame
pygame.init()

DB.create_database()

font = pygame.font.Font(r"assets\fonts\RubikDistressed-Regular.ttf", 30)
pygame.display.set_icon(logo)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic space")
sound = Sound()
burans = Burans(enemy_burans, player)


# Главное меню
def main_menu():
    global frame_start_index, sound_on
    frame_delay = 50
    high_scores = DB.read_high_scores()
    while True:
        Render.draw_png(background_start, screen, frame_start_index, WIDTH, HEIGHT)
        
        Render.draw_text("TRAFFIC SPACE", font, BLACK, screen, WIDTH // 2, 100)

        # Кнопки
        mx, my = pygame.mouse.get_pos()
        button_start = pygame.Rect(WIDTH // 2 - 150, 200, 300, 50)
        button_instructions = pygame.Rect(WIDTH // 2 - 150, 300, 300, 50)
        button_quit = pygame.Rect(WIDTH // 2 - 150, 400, 300, 50)
        button_sound = pygame.Rect(WIDTH - 70, 20, 50, 50)

        pygame.draw.rect(screen, GREEN if button_start.collidepoint((mx, my)) else BLACK, button_start, border_radius=button_border_radius)
        pygame.draw.rect(screen, GREEN if button_instructions.collidepoint((mx, my)) else BLACK, button_instructions, border_radius=button_border_radius)
        pygame.draw.rect(screen, GREEN if button_quit.collidepoint((mx, my)) else BLACK, button_quit, border_radius=button_border_radius)
        pygame.draw.rect(screen, GRAY if sound.volume_level == 0 else GREEN, button_sound, border_radius=circle_border_radius)
        
        if len(high_scores) > 0:
            for i, j in zip(range(len(high_scores)), range(3)):
                score = high_scores[i]
                Render.draw_text(f"{i + 1}. {score}", font, BLACK, screen, 70, 30 + i * 30)
                
        Render.draw_text("Начать", font, WHITE, screen, WIDTH // 2, 225)
        Render.draw_text("Инструкция", font, WHITE, screen, WIDTH // 2, 325)
        Render.draw_text("Выйти", font, WHITE, screen, WIDTH // 2, 425)
        
        if sound.volume_level == 1:
            screen.blit(sound_icon_on, (WIDTH - 57, 33))  # Иконка звука включена
        elif sound.volume_level == 0.5:
            screen.blit(sound_icon_on_off, (WIDTH - 57, 33))  # Иконка звука выключена
        elif sound.volume_level == 0:
            screen.blit(sound_icon_off, (WIDTH - 57, 33))  # Иконка звука выключена
        
        frame_start_index = (frame_start_index + 1) % frame_start_count
        pygame.time.delay(frame_delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint((mx, my)):
                    sound.play_button_sound()
                    difficulty_menu()
                if button_instructions.collidepoint((mx, my)):
                    sound.play_button_sound()
                    instructions()
                if button_quit.collidepoint((mx, my)):
                    sound.play_button_sound()
                    pygame.quit()
                    sys.exit()
                if button_sound.collidepoint((mx, my)):  # Переключение звука
                    sound.play_button_sound()
                    sound.toggle_sound()  

        pygame.display.flip()
        clock.tick(FPS)


# Меню выбора сложности
def difficulty_menu():
    while True:
        screen.blit(background_level, (0, 0))
        Render.draw_text("Выберите сложность", font, BLACK, screen, WIDTH // 2, 100)

        # Кнопки
        mx, my = pygame.mouse.get_pos()
        button_easy = pygame.Rect(WIDTH // 2 - 100, 200, 200, 50)
        button_medium = pygame.Rect(WIDTH // 2 - 100, 300, 200, 50)
        button_hard = pygame.Rect(WIDTH // 2 - 100, 400, 200, 50)
        button_back = pygame.Rect(20, 20, 50, 50)

        pygame.draw.rect(screen, GREEN if button_easy.collidepoint((mx, my)) else BLACK, button_easy, border_radius=button_border_radius)
        pygame.draw.rect(screen, ORANGE if button_medium.collidepoint((mx, my)) else BLACK, button_medium, border_radius=button_border_radius)
        pygame.draw.rect(screen, RED if button_hard.collidepoint((mx, my)) else BLACK, button_hard, border_radius=button_border_radius)
        pygame.draw.rect(screen, GREEN if button_back.collidepoint((mx, my)) else BLACK, button_back, border_radius=circle_border_radius)
        screen.blit(back_icon, (33, 33)) 

        Render.draw_text("Легкий", font, WHITE, screen, WIDTH // 2, 225)
        Render.draw_text("Средний", font, WHITE, screen, WIDTH // 2, 325)
        Render.draw_text("Сложный", font, WHITE, screen, WIDTH // 2, 425)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.collidepoint((mx, my)):
                    sound.play_button_sound()
                    game_loop("Легкий")
                if button_medium.collidepoint((mx, my)):
                    sound.play_button_sound()
                    game_loop("Средний")
                if button_hard.collidepoint((mx, my)):
                    sound.play_button_sound()
                    game_loop("Сложный")
                if button_back.collidepoint((mx, my)):
                    sound.play_button_sound()
                    return  # Возвращаемся в главное меню

        pygame.display.flip()
        clock.tick(FPS)

# Инструкции
def instructions():    
    while True:
        screen.blit(background_rule, (0, 0))
        
        mx, my = pygame.mouse.get_pos()
        button_back = pygame.Rect(20, 20, 50, 50)
        
        pygame.draw.rect(screen, GREEN if button_back.collidepoint((mx, my)) else BLACK, button_back, border_radius=circle_border_radius)
        screen.blit(back_icon, (33, 33)) 


        Render.draw_text("Управляйте самолетом с помощью стрелок", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 50)
        Render.draw_text("Избегайте столкновений с метеоритами", font, WHITE, screen, WIDTH // 2, HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левый клик мыши
                    if button_back.collidepoint((mx, my)):
                        sound.play_button_sound()
                        return  # Возвращаемся в главное меню


        pygame.display.flip()
        clock.tick(FPS)


pause_background = None  # Переменная для хранения фона во время паузы

# Функция паузы
def pause_menu(): 
    while True:
        if pause_background:
            screen.blit(pause_background, (0, 0))  # Отображаем сохраненное изображение
        
        Render.draw_text("ПАУЗА", font, BLACK, screen, WIDTH // 2, 200)
        # Кнопки
        mx, my = pygame.mouse.get_pos()
        button_continue = pygame.Rect(WIDTH // 2 - 150, 250, 300, 50)
        button_exit = pygame.Rect(WIDTH // 2 - 150, 350, 300, 50)
        button_sound = pygame.Rect(WIDTH - 70, 20, 50, 50)

        pygame.draw.rect(screen, GREEN if button_continue.collidepoint((mx, my)) else BLACK, button_continue, border_radius=button_border_radius)
        pygame.draw.rect(screen, GREEN if button_exit.collidepoint((mx, my)) else BLACK, button_exit, border_radius=button_border_radius)
        pygame.draw.rect(screen, GRAY if sound.volume_level == 0 else GREEN, button_sound, border_radius=circle_border_radius)
                
        Render.draw_text("Продолжить", font, WHITE, screen, WIDTH // 2, 275)
        Render.draw_text("Завершить", font, WHITE, screen, WIDTH // 2, 375)
                
        if sound.volume_level == 1:
            screen.blit(sound_icon_on, (WIDTH - 57, 33))  # Иконка звука включена
        elif sound.volume_level == 0.5:
            screen.blit(sound_icon_on_off, (WIDTH - 57, 33))  # Иконка звука выключена
        elif sound.volume_level == 0:
            screen.blit(sound_icon_off, (WIDTH - 57, 33))  # Иконка звука выключена
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_continue.collidepoint((mx, my)):
                    sound.play_button_sound()
                    return resume_game()  # Закрываем меню паузы и начинаем отсчет
                if button_exit.collidepoint((mx, my)):
                    sound.play_button_sound()
                    return main_menu()  # Переходим в главное меню
                if button_sound.collidepoint((mx, my)):  # Переключение звука
                    sound.play_button_sound()
                    sound.toggle_sound()  

        pygame.display.flip()
        clock.tick(FPS)


def resume_game():
    pause_time = 3  # Время задержки в секундах
    start_ticks = pygame.time.get_ticks()  # Время начала отсчета
    while True:
        if pause_background:
            screen.blit(pause_background, (0, 0))  # Отображаем сохраненное изображение


        seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # Для отсчета времени
        
        Render.draw_text(f"Игра продолжится через {pause_time - seconds}", font, WHITE, screen, WIDTH // 2, HEIGHT // 2)

        if seconds >= pause_time:
            sound.traffic_sound.play(-1)
            break  # Таймер завершился

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

# Вызов функции pause_menu() в game_loop()
def game_loop(difficulty):
    global frame_traffic_index, explosion_active, frame_boom_index, explosion_pos, get_money_active
    score = 0
    burans.enemies = []
    spawn_timer = 0
    explosion_active = False  
    global pause_background
    get_money_active = False

    # Определяем скорость в зависимости от сложности
    speed_factor = 0.5 if difficulty == "Легкий" else 0.8 if difficulty == "Средний" else 1.2 
    
    sound.traffic_sound.play(-1)

    while True:     
        frame_traffic_index = (frame_traffic_index + speed_factor) % frame_traffic_count
        if explosion_active:
            frame_boom_index = (frame_boom_index + 1) % frame_boom_count
            
        Render.draw_png(background_traffic, screen, int(frame_traffic_index), WIDTH, HEIGHT)

        Render.draw_text(f"Score: {score} ", font, RED, screen, WIDTH // 2, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Управление игроком
        keys = pygame.key.get_pressed()
        burans.player_move(keys)

        # Перед вызовом pause_menu():
        if keys[pygame.K_ESCAPE]:
            pause_background = pygame.display.get_surface().copy()  # Сохраняем текущее состояние экрана
            sound.traffic_sound.stop()
            pause_menu()  # Пауза

        # Спавн врагов
        spawn_timer += 1
        if spawn_timer > 30:
            burans.spawn_enemy()
            spawn_timer = 0

        # Обновление врагов
        for enemy in burans.enemies:
            enemy_rect, enemy_car = enemy
            enemy_rect.y += enemy_speed[difficulty]
            if enemy_rect.top > HEIGHT:
                burans.enemies.remove(enemy)

        #обновление денег
        for money in burans.money:
            money_rect, enemy_money = money
            money_rect.y += enemy_speed[difficulty]
            if money_rect.top > HEIGHT:
                burans.money.remove(money)

        # проверка получения денег
        for money in burans.money:
            if player.colliderect(money[0]):
                get_money_active = True
                burans.money.remove(money)
                explosion_pos = player.topleft
                break

        # Проверка столкновений
        for enemy in burans.enemies:
            if player.colliderect(enemy[0]):
                explosion_active = True
                explosion_pos = player.topleft
                break

        #увелечение счетчика денег
        if get_money_active:
            get_money_active = False
            sound.button_sound_1.play()
            score += 1

        # Отрисовка взрыва
        if explosion_active:
            sound.traffic_sound.stop()
            Render.draw_png(background_boom, screen, frame_boom_index, WIDTH, HEIGHT)
            sound.play_sound_boom()
            if frame_boom_index == frame_boom_count - 1:
                explosion_active = False
                frame_boom_index = 0
                DB.saveData(score)
                return main_menu()

        # Отрисовка самолета, если нет взрыва
        if not explosion_active:
            screen.blit(player_buran, player.topleft)
            for enemy in burans.enemies:
                enemy_rect, enemy_car = enemy
                screen.blit(enemy_car, enemy_rect.topleft)
            for money in burans.money:
                money_rect, enemy_money = money
                screen.blit(enemy_money, money_rect.topleft)


        pygame.display.flip()
        clock.tick(FPS)

# Запуск игры
main_menu()
