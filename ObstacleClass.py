import pygame

collide_list = []

#Enemies or obstacles which will move in a straight path
class ObstacleClass():
    def __init__(self, startx: int, starty: int, speedx: int, speedy: int, width: int, height: int, collision: bool, frames: list, descriptor: str):
        self.collision = collision
        self.xcor = startx
        self.ycor = starty
        self.speedx = speedx
        self.speedy = speedy
        self.width = width
        self.height = height
        self.descriptor = descriptor
        self.images = []
        for image in frames:
            self.image = pygame.transform.scale(image, (width * 4, height * 4))
            self.images.append(self.image)
        self.frame_num = 0
        self.Rect = pygame.Rect(startx, starty, self.width, self.height)
        


    def move(self):
        self.xcor -= self.speedx
        self.ycor -= self.speedy
        self.Rect = pygame.Rect(self.xcor, self.ycor, self.width, self.height)

    def update_frame(self):
        self.frame_num += 1
        if self.frame_num == len(self.images):
            self.frame_num = 0
        self.image = self.images[self.frame_num]