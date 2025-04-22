import pygame

# constants

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 600
SCREEN_WIDTH_CENTER = SCREEN_WIDTH / 2
SCREEN_HEIGHT_CENTER = SCREEN_HEIGHT / 2

PoppinsFont = "Poppins-Medium.ttf"

class TextClass():
    def __init__(self, textString:str, textFont:pygame.font.Font, textColor:list, textPos:tuple):
        self.textString = textString
        self.textFont = textFont
        self.textRender = textFont.render(textString, True, textColor)
        self.textPos = textPos
        self.textRect = None
        
    def blit(self):
        self.textRect = self.textRender.get_rect(center = self.textPos)
        self.resultText = screen.blit(self.textRender, self.textRect)


class ButtonClass():
    def __init__(self, btnText:TextClass, btnRect:pygame.Rect, btnLineWidth:int, bgColor:list):
        self.btnText = btnText
        self.btnRect = btnRect
        self.btnLineWidth = btnLineWidth
        self.bgColor = bgColor
        
    def draw(self):
        self.rectangleRender = pygame.draw.rect(screen, self.bgColor, self.btnRect)
        self.btnText.blit()


class Bird():
    def __init__(self, xcor, ycor):
        # animation if willing to add
        self.birdRect = pygame.Rect((xcor, ycor), (256, 256))
        sprite_sheet = pygame.image.load("PigeonAsset/pigeon_fiy-Sheet.png")
        self.frame_width, self.frame_height = 32, 32
        self.frames = []
        for i in range(sprite_sheet.get_width() // self.frame_width):
            self.frame = sprite_sheet.subsurface(pygame.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height))
            self.frame = pygame.transform.scale(self.frame, size= (64, 64))
            self.frames.append(self.frame)
        self.frame_count = 0
        self.current_frame = self.frames[self.frame_count]

    def animation_update(self):
        self.frame_count += 1
        if self.frame_count == len(self.frames):
            self.frame_count = 0
        self.current_frame = self.frames[self.frame_count]
        print(self.frame_count)
        

        

        

    def move(self):
        pass



        
def CreateButton():
    pass

pygame.init()
pygame.display.set_caption("Animal Journey")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GameState = "BirdLevel"




bird = Bird(50, 50)

RunVar = True
while RunVar == True:
    match GameState:
        case "TitleScreen":
            screen.fill(WHITE)
            
            titleText = TextClass("Animal Journey", pygame.font.Font(PoppinsFont, 50), BLACK, (SCREEN_WIDTH_CENTER, 175))
            titleText.blit()
            
            startButton = ButtonClass(TextClass("Start", pygame.font.Font(PoppinsFont, 20), BLACK, (SCREEN_WIDTH_CENTER, 225)), pygame.Rect(SCREEN_WIDTH_CENTER - 50, 225 - 25, 100, 50), 0, GREEN)
            startButton.draw()
            
        case "EndScreen":
            screen.fill(WHITE)
            

        #commented because of run error
        # case _:
        #     #default
        #     pass

        case "BirdLevel":
            screen.fill(BLUE)
            
            
            screen.blit(bird.current_frame, bird.birdRect)
            bird.animation_update()
        
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunVar = False
            
    pygame.display.update()
    
    pygame.time.Clock().tick(15)

pygame.quit()