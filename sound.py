import pygame
pygame.mixer.init()
mixer = pygame.mixer

class SoundClass:
    def __init__(self):
        # self.win = mixer.Sound("SOUNDPATH.wav")
        self.sound_dict = {
            "Win": mixer.Sound("SoundFiles/Win.mp3")
        }

    def play(*sounds):
        for sound in sounds:
            pass


sound = SoundClass()
sound.sound_dict['Win'].play()