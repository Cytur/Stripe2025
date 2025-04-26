import pygame



class Lives():
    def __init__(self):
        self.heart_img = pygame.image.load("HeartAsset/Heart.png")
        self.lives = []
        
        
        

    def remove_life(self):
        try:
            self.lives.pop(-1)
            if len(self.lives) == 0:
                return True
        except:
            pass

    def load_hearts(self, lives_num):
        if len(self.lives) == 0:
            self.lives = [(self.heart_img, pygame.Rect((50 + x*50, 50), (64, 64))) for x in range(lives_num)]