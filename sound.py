import pygame
pygame.mixer.init()
mixer = pygame.mixer

class SoundClass:
    def __init__(self):
        # self.win = mixer.Sound("SOUNDPATH.wav")
        pass

    def play(*sounds):
        for sound in sounds:
            sound.play()