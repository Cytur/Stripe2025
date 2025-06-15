import pygame
pygame.mixer.init()
mixer = pygame.mixer

class SoundClass:
    def __init__(self):
        # self.win = mixer.Sound("SOUNDPATH.wav")
        self.sound_dict = {
            "Win": mixer.Sound("SoundFiles/Win.wav"),
            "Collision": mixer.Sound("SoundFiles/Collision.wav"),
            "Lose" : mixer.Sound("SoundFiles/Lose.wav"),
            "Flap" : mixer.Sound("SoundFiles/Flap.wav"),
            "Trot" : mixer.Sound("SoundFiles/Trot.wav"),
            "Swim" : mixer.Sound("SoundFIles/Swim.wav"),
        }
        pygame.mixer.Sound.set_volume(self.sound_dict["Flap"], 200)
        pygame.mixer.Sound.set_volume(self.sound_dict["Swim"], 2000)
        mixer.music.load("SoundFiles\Music.mp3")

    def play(self, *sounds):
        for sound in sounds:
            try:
                self.sound_dict[f"{sound}"].play()
            except:
                pass

    def play_backround_music(self):
        pygame.mixer.music.play(-1)

