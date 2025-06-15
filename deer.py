import pygame
import DesignClass

class Deer():
    def __init__(self, xcor:int, ycor:int, frames):
        self.speed = 10
        self.xcor = xcor
        self.ycor = ycor
        self.Rect = pygame.Rect((self.xcor, self.ycor), (28*4, 100))
        
        self.frames = frames

        self.icon = pygame.image.load("ImageAssets/DeerAsset/deer_icon.png")

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
        
    def show_hitbox(self, screen):
        pygame.draw.rect(screen, DesignClass.Colors["GREEN"], self.Rect)