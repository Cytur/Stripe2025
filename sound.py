import pygame
pygame.mixer.init()
mixer = pygame.mixer

class SoundClass:
    def __init__(self):
        # self.win = mixer.Sound("SOUNDPATH.wav")
        self.sound_dict = {
            "Win": mixer.Sound("SoundFiles/Win.wav"),
            # "Lose": mixer.Sound("Sound")
        }
        mixer.music.load("SoundFiles\Music.mp3")

    def play(self, *sounds):
        for sound in sounds:
            try:
                self.sound_dict[f"{sound}"].play()
            except:
                pass

    def play_backround_music(self):
        pygame.mixer.music.play(-1)

