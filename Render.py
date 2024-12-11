import pygame
import random
import sys
import sqlite3
from PIL import Image


class Render:
    def draw_png(images, screen, frame_index, width, height):
        frame = images[frame_index]
        frame_scaled = pygame.transform.scale(frame, (width, height))
        screen.blit(frame_scaled, (0, 0))
    
    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    def load_bg(filename):
        image = Image.open(filename)
        frames = []
        try:
            while True:
                frame = image.copy()
                frame = frame.convert("RGBA")  # Конвертация в RGBA для Pygame
                frame_data = frame.tobytes("raw", "RGBA")
                frame_surface = pygame.image.fromstring(frame_data, frame.size, "RGBA")
                frames.append(frame_surface)
                image.seek(image.tell() + 1)
        except EOFError:
            pass  # Останавливаемся, когда добираемся до конца GIF
        return frames