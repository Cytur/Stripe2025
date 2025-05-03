import pygame



class Lives():
    def __init__(self):
        self.heart_img = pygame.transform.scale(pygame.image.load("HeartAsset/Heart.png"), (100, 100))
        self.lives = []
        self.lost_lives = []
        self.lives_num = 0
        
        
    def remove_life(self):
        try:
            self.lives.pop(-1)
            self.lives_num -= 1
            if len(self.lives) == 0:
                return True
        except:
            pass


    def add_hearts(self, heartsToAdd):
        self.lives_num += heartsToAdd
        self.lives = [] #To reset the lives
        self.load_hearts(self.lives_num)


    def load_hearts(self, lives_num):
        if len(self.lives) == 0:
            self.lives_num = lives_num
            self.lives = [(self.heart_img, pygame.Rect((50 + x*50, 50), (64, 64))) for x in range(lives_num)]

    def blit(self, screen):
        for heart in self.lives:
            img = heart[0]
            rect = heart[1]
            screen.blit(img, rect)