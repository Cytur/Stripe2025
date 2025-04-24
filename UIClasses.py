import pygame

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