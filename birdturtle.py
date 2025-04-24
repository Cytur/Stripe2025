import pygame

#The bird and turtle have similar movement

class BirdTurtle():
    def __init__(self, xcor:int, ycor:int, frame_list:list):
        self.speed = 10
        self.xcor = xcor
        self.ycor = ycor
        self.Rect = pygame.Rect((self.xcor, self.ycor), (288, 288))

        self.frames = frame_list
        self.frame_count = 0
        self.current_frame = self.frames[self.frame_count]

    def animation_update(self):
        self.frame_count += 1
        if self.frame_count == len(self.frames):
            self.frame_count = 0
        self.current_frame = self.frames[self.frame_count]


    def move(self, direction):
        if direction == "UP":
            self.ycor -= self.speed

        if direction == "DOWN":
            self.ycor += self.speed


        self.Rect = pygame.Rect((self.xcor, self.ycor), (256, 256))

        direction = ""