import pygame
import DesignClass

collide_list = []

#Enemies or obstacles which will move in a straight path
class ObstacleClass():
    def __init__(self, startx: int, starty: int, speedx: int, speedy: int, width: int, height: int, rectwidth: int, rectheight: int, collision: bool, kill: bool, frames: list, descriptor: str):
        self.collision = collision
        self.kill = kill
        self.xcor = startx
        self.ycor = starty
        self.speedxdefault = speedx
        self.speedydefault = speedy
        self.speedx = speedx
        self.speedy = speedy
        self.width = width
        self.height = height
        self.rectwidth = rectwidth
        self.rectheight = rectheight
        self.descriptor = descriptor
        self.images = []
        for image in frames:
            self.image = pygame.transform.scale(image, (width * 4, height * 4))
            self.images.append(self.image)
        self.frame_num = 0
        self.Rect = pygame.Rect(startx, starty, self.rectwidth * 2, self.rectheight* 2)


    def move(self):
        self.xcor -= self.speedx
        self.ycor -= self.speedy
        self.Rect = pygame.Rect(self.xcor, self.ycor, self.rectwidth * 2, self.rectheight * 2)

    def update_frame(self):
        self.frame_num += 1
        if self.frame_num == len(self.images):
            self.frame_num = 0
        self.image = self.images[self.frame_num]

    def show_hitbox(self, screen):
        pygame.draw.rect(screen, DesignClass.Colors["GREEN"], self.Rect)