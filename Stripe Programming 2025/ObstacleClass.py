import pygame

#Enemies or obstacles which will move in a straight path
class ObstacleClass():
    def __init__(self, startx: int, starty: int, speed: int, image: pygame.Surface, width: int, height: int, collision: bool):
        self.collision = collision
        self.xcor = startx
        self.ycor = starty
        self.speed = speed
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(startx, starty, self.width, self.height)
        self.image = pygame.transform.scale(image, (width, height))

    def move(self):
        self.xcor -= self.speed
        self.rect = pygame.Rect(self.xcor, self.ycor, self.width, self.height)