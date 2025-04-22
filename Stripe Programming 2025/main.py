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


#Enemies or obstacles which will move in a straight path
class ObstacleClass():
    def __init__(self, startx: int, starty: int, speed: int, image: pygame.Surface, width: int, height: int):
        self.xcor = startx
        self.ycor = starty
        self.speed = speed
        self.width = width
        self.height = height
        self.rect = pygame.Rect(startx, starty, self.width, self.height)
        self.image = pygame.transform.scale(image, (width, height))

    def move(self):
        self.xcor -= self.speed
        self.rect = pygame.Rect(self.xcor, self.ycor, self.width, self.height)


class Bird():
    def __init__(self, xcor:int, ycor:int):
        self.speed = 10
        self.xcor = xcor
        self.ycor = ycor
        self.birdRect = pygame.Rect((self.xcor, self.ycor), (256, 256))
        self.frame_width, self.frame_height = 32, 32

        # Loading all bird frames into a list
        self.frames = []
        for num in range(8):
            frame = pygame.image.load(f"BirdAsset/BirdFlying{num+1}.png")
            frame = pygame.transform.scale(frame, size= (64, 64))
            frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
            self.frames.append(frame)

        
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


        self.birdRect = pygame.Rect((self.xcor, self.ycor), (256, 256))

        direction = ""



        
def CreateButton():
    pass

pygame.init()
pygame.display.set_caption("Animal Journey")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GameState = "BirdLevel"




bird = Bird(50, 50)
# turtle = Turtle(x, y)
# deer = Deer(x, y)

obstacle_list = []

message_end_time = 0

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
            current_player = bird
            screen.fill(BLUE)
            
                



            screen.blit(bird.current_frame, bird.birdRect)
            
            current_time = pygame.time.get_ticks()

            if current_time > message_end_time:
                bird.animation_update()
                message_end_time = pygame.time.get_ticks() + 50





    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunVar = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            current_player.move("UP")
        if keys[pygame.K_s]:
            current_player.move("DOWN")

        # if animal will have left and right
        if keys[pygame.K_a]:
            current_player.move("LEFT")
        if keys[pygame.K_s]:
            current_player.move("RIGHT")
            
    pygame.display.update()
    
    pygame.time.Clock().tick(60)

pygame.quit()