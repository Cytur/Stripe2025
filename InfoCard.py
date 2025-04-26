import pygame
import DesignClass
from UIClasses import TextClass, ButtonClass


class InfoCard():
    def __init__(self, Title: str, Description1:str, Description2, Challenges:str, migrationpattern: str, xcor, ycor, icon: pygame.Surface, bg: tuple, y_offset, screen, gamestatefunc, gamestate: str):
        self.screen = screen

        self.title = Title
        #splitting the description into 2 lines to fit onto info card
        self.des1 = Description1
        self.des2 = Description2
        self.challenges = Challenges
        self.migpat = migrationpattern

        self.width = 200
        self.height = 300
        self.xcor = xcor - self.width/2
        self.ycor = ycor - self.height/2

        self.icon = pygame.transform.scale2x(icon)
        self.bg = bg
        self.icon_y_offset = y_offset

        self.iconRect = pygame.Rect(self.xcor, self.ycor + 60 - self.icon_y_offset, 96*2, 96*2)
        self.playbutton = ButtonClass(TextClass("Start", pygame.font.Font(DesignClass.Fonts["Poppins"], 20), DesignClass.Colors["BLACK"], (self.xcor + self.width/2, self.ycor + 300 - 15), screen), pygame.Rect(self.xcor, self.ycor + 300 - 30, 200, 30), 0, DesignClass.Colors["GREEN"], screen, gamestatefunc, gamestate)
        self.desText1 = TextClass(self.des1, pygame.font.Font(DesignClass.Fonts["Poppins"], 9), DesignClass.Colors["BLACK"], (self.xcor + self.width/2, self.ycor + self.height - 80), self.screen)
        self.desText2 = TextClass(self.des2, pygame.font.Font(DesignClass.Fonts["Poppins"], 9), DesignClass.Colors["BLACK"], (self.xcor + self.width/2, self.ycor + self.height - 70), self.screen)
        self.migpatText = TextClass(self.migpat, pygame.font.Font(DesignClass.Fonts["Poppins"], 9), DesignClass.Colors["BLACK"], (self.xcor + self.width/2, self.ycor + self.height - 50), self.screen)
        self.titleText = TextClass(self.title, pygame.font.Font(DesignClass.Fonts["Poppins"], 15), DesignClass.Colors["BLACK"], (self.xcor + self.width/2, self.ycor + 15), self.screen)
        

    def show(self, Screen: pygame.Surface):
        self.card_rect = pygame.draw.rect(Screen, self.bg, pygame.Rect(self.xcor, self.ycor, self.width, self.height))
        # print(self.ycor, self.xcor)
        self.titleText.blit()
        self.desText1.blit()
        self.desText2.blit()
        self.migpatText.blit()
        self.playbutton.draw()
        Screen.blit(self.icon, self.iconRect)