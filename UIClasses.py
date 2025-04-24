import pygame

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
SKYBLUE = [170,206,250]
OCEANBLUE = [1,84,130]
OCEANYELLOW = (128,128,0)
GRASSGREEN = (0,154,23)

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 600
SCREEN_WIDTH_CENTER = SCREEN_WIDTH / 2
SCREEN_HEIGHT_CENTER = SCREEN_HEIGHT / 2



class TextClass():
    def __init__(self, textString:str, textFont:pygame.font.Font, textColor:list, textPos:tuple, screen: pygame.Surface):
        self.textString = textString
        self.textFont = textFont
        self.textRender = textFont.render(textString, True, textColor)
        self.textPos = textPos
        self.textRect = None
        self.screen = screen
        
    def blit(self):
        self.textRect = self.textRender.get_rect(center = self.textPos)
        self.resultText = self.screen.blit(self.textRender, self.textRect)


class ButtonClass():
    def __init__(self, btnText:TextClass, btnRect:pygame.Rect, btnLineWidth:int, bgColor:list, screen: pygame.Surface, command, param):
        self.btnText = btnText
        self.btnRect = btnRect
        self.btnLineWidth = btnLineWidth
        self.bgColor = bgColor
        self.screen = screen
        self.command = command
        self.param = param
        
    def draw(self):
        self.rectangleRender = pygame.draw.rect(self.screen, self.bgColor, self.btnRect)
        self.btnText.blit()