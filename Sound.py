import pygame
from constants import *

class Sound:
    def __init__(self):
        self.button_sound_1 = pygame.mixer.Sound(r"assets\music\button-sound1.mp3")
        self.sound_boom = pygame.mixer.Sound(r"assets\music\sound-booms.mp3")
        self.volume_level = 1.0
        self.traffic_sound = pygame.mixer.Sound(r"assets\music\traffic-sound.mp3")
        pygame.mixer.music.load(r"assets\music\background-sound.mp3") 
        pygame.mixer.music.play(-1)

    def play_button_sound(self):
        self.button_sound_1.play()

    def play_sound_boom(self):
        self.sound_boom.play()
    
    def toggle_sound(self):
        self.volume_level -= 0.5 
        if self.volume_level == -0.5:
            self.volume_level = 1
        pygame.mixer.music.set_volume(self.volume_level)
