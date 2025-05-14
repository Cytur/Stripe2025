import pygame

class Deer():
    def __init__(self, xcor:int, ycor:int):
        self.speed = 10
        self.xcor = xcor
        self.ycor = ycor
        self.Rect = pygame.Rect((self.xcor, self.ycor), (28*4, 100))
        
        self.frames = []

        self.icon = pygame.image.load("DeerAsset/deer_icon.png")

        for img in range(5):
            image=pygame.image.load(f'DeerAsset/deer{img+1}.png')
            image = pygame.transform.scale(image, (28*4, 100))
            self.frames.append(image)

        self.framesRev = [pygame.transform.flip(x, True, False) for x in self.frames]
        

        self.frame_count = 0
        self.cur_frames = self.frames
        self.current_frame = self.frames[self.frame_count]

    def animation_update(self):
        self.frame_count += 1
        if self.frame_count == len(self.frames):
            self.frame_count = 0
        self.current_frame = self.cur_frames[self.frame_count]


    def jump(self, yIncrement):
        self.ycor -= yIncrement

        self.Rect = pygame.Rect((self.xcor, self.ycor), (28*4, 100))

    def move(self, direction):
        if direction == "RIGHT":

            self.xcor += self.speed

            self.cur_frames = self.frames

        if direction == "LEFT":
            self.xcor -= self.speed

            self.cur_frames = self.framesRev

        if direction == "DOWN":
            self.ycor += self.speed

        if direction == "UP":
            self.ycor -= self.speed

        self.Rect = pygame.Rect((self.xcor, self.ycor), (28*4, 100))

        direction = ""

    def blit(self, screen):
        screen.blit(self.current_frame, self.Rect)

    def rect_update(self):
        self.Rect = pygame.Rect((self.xcor, self.ycor), (28*4, 100))
        