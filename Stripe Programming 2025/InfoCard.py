import pygame
from UIClasses import TextClass, ButtonClass


BLACK = [0,0,0]


PoppinsFont = "Poppins-Medium.ttf"


class InfoCard():
    def __init__(self, txt: TextClass, btn: ButtonClass, Title: str, Description1:str, Description2, Challenges:str, xcor, ycor, icon: pygame.Surface, bg: tuple, y_offset, screen):
        self.title = Title
        self.screen = screen
        #splitting the description into 2 lines to fit onto info card
        self.des1 = Description1
        self.des2 = Description2
        self.challenges = Challenges
        self.width = 200
        self.height = 200
        self.xcor = xcor - self.width/2
        self.ycor = ycor - self.height/2
        self.txt = txt
        self.icon = pygame.transform.scale2x(icon)
        self.bg = bg
        self.icon_y_offset = y_offset
        self.iconRect = pygame.Rect(self.xcor, self.ycor + 20 - self.icon_y_offset, 96*2, 96*2)
        self.desText1 = self.txt(self.des1, pygame.font.Font(PoppinsFont, 9), BLACK, (self.xcor + self.width/2, self.ycor + self.height - 30), self.screen)
        self.desText2 = self.txt(self.des2, pygame.font.Font(PoppinsFont, 9), BLACK, (self.xcor + self.width/2, self.ycor + self.height - 20), self.screen)
        self.titleText = self.txt(self.title, pygame.font.Font(PoppinsFont, 15), BLACK, (self.xcor + self.width/2, self.ycor + 15), screen)
        

    def show(self, Screen: pygame.Surface):
        self.card_rect = pygame.draw.rect(Screen, self.bg, pygame.Rect(self.xcor, self.ycor, self.width, self.height))
        # print(self.ycor, self.xcor)
        self.titleText.blit()
        self.desText1.blit()
        self.desText2.blit()
        Screen.blit(self.icon, self.iconRect)