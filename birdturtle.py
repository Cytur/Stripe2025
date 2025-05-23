import pygame
import DesignClass

#The bird and turtle have similar movement

class BirdTurtle():
    def __init__(self, xcor:int, ycor:int, frame_list:list, sizex, sizey):
        self.speed = 20
        self.sizex = sizex
        self.sizey = sizey
        self.xcor = xcor
        self.ycor = ycor
        self.Rect = pygame.Rect((self.xcor, self.ycor), (self.sizex, self.sizey))

        self.frames = frame_list
        self.frame_count = 0
        self.cur_frames = self.frames
        self.current_frame = self.frames[self.frame_count]

        self.framesRev = [pygame.transform.flip(x, True, False) for x in self.frames]

    def animation_update(self):
        self.frame_count += 1
        if self.frame_count == len(self.frames):
            self.frame_count = 0
        self.current_frame = self.cur_frames[self.frame_count]


    def move(self, direction):
        if direction == "UP":
            self.ycor -= self.speed
            self.cur_frames = self.frames

        if direction == "DOWN":
            self.ycor += self.speed
            self.cur_frames = self.frames

        #FOR NPCs
        if direction == "RIGHT":

            self.xcor += self.speed

            self.cur_frames = self.frames

        if direction == "LEFT":
            self.xcor -= self.speed

            self.cur_frames = self.framesRev


        self.Rect = pygame.Rect((self.xcor, self.ycor), (self.sizex, self.sizey))

        direction = ""

    def rect_update(self):
        self.Rect = pygame.Rect((self.xcor, self.ycor), (self.sizex, self.sizey))

    def show_hitbox(self, screen):
        pygame.draw.rect(screen, DesignClass.Colors["GREEN"], self.Rect)