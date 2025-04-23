import pygame
import random

# constants

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
SKYBLUE = [170,206,250]
OCEANBLUE = [1,84,130]

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


class InfoCard():
    def __init__(self, txt: TextClass, btn: ButtonClass, Title: str, Description:str, Challenges:str, xcor, ycor, icon: pygame.Surface, bg: tuple):
        self.title = Title
        self.des = Description
        self.challenges = Challenges
        self.width = 200
        self.height = 400
        self.xcor = xcor - self.width/2
        self.ycor = ycor - self.height/2
        self.txt = txt
        self.icon = icon
        self.bg = bg

    def show(self, Screen):
        self.card_rect = pygame.draw.rect(Screen, self.bg, pygame.Rect(self.xcor, self.ycor, self.width, self.height))
        print(self.ycor, self.xcor)
        titleText = self.txt(self.title, pygame.font.Font(PoppinsFont, 10), BLACK, (self.xcor + self.width/2, self.ycor + 15))
        titleText.blit()
        desText = self.txt(self.title, pygame.font.Font(PoppinsFont, 5), BLACK, (self.xcor, self.ycor+30))



#Enemies or obstacles which will move in a straight path
class ObstacleClass():
    def __init__(self, startx: int, starty: int, speed: int, image: pygame.Surface, width: int, height: int, collision: bool):
        self.collision = collision
        self.xcor = startx
        self.ycor = starty
        self.speed = speed
        self.width = width
        self.height = height
        self.image = image
        self.rect = pygame.Rect(startx, starty, self.width, self.height)
        self.image = pygame.transform.scale(image, (width, height))

    def move(self):
        self.xcor -= self.speed
        self.rect = pygame.Rect(self.xcor, self.ycor, self.width, self.height)


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



        
def CreateButton():
    pass

pygame.init()
pygame.display.set_caption("Animal Journey")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


bird_frames = []
turt_frames = []

for num in range(8):
            frame = pygame.image.load(f"BirdAsset/BirdFlying{num+1}.png")
            frame = pygame.transform.scale(frame, size= (64, 64))
            frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
            bird_frames.append(frame)

for num in range(6):
            frame = pygame.image.load(f"TurtleAsset/24bit-seaturtle{num+1}.png")
            frame = pygame.transform.scale(frame, size= (96, 96))
            frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
            turt_frames.append(frame)

bird = BirdTurtle(50, 50, bird_frames)
turtle = BirdTurtle(50, 50, turt_frames)
# deer = Deer(x, y)

turtle_info = InfoCard(TextClass, ButtonClass, "Leather-Back Sea Turtle", "The largest sea turtle in the world, one that travels thousands of kilometers",
                       "Pollution, Sharks, Orcas", SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, turt_frames[0], OCEANBLUE)

bird_info = InfoCard(TextClass, ButtonClass, "Red Winged Blackbird", "A stocky, red and black bird, and one that is very common in North America.",
                     " Air pollution, Hawks, Eagles", SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, bird_frames[0], SKYBLUE)

obstacle_list = []
cloud_img_list = ["CloudAsset/Cloud 10.png", "CloudAsset/Cloud 11.png", "CloudAsset/Cloud 12.png"]

end_time_player_animation = 0
end_time_cloud_animation = 0

GameState = "PlayerChoose"

RunVar = True
while RunVar == True:
    match GameState:
        case "TitleScreen":
            screen.fill(WHITE)
            
            titleText = TextClass("Animal Journey", pygame.font.Font(PoppinsFont, 50), BLACK, (SCREEN_WIDTH_CENTER, 175))
            titleText.blit()
            
            startButton = ButtonClass(TextClass("Start", pygame.font.Font(PoppinsFont, 20), BLACK, (SCREEN_WIDTH_CENTER, 225)), pygame.Rect(SCREEN_WIDTH_CENTER - 50, 225 - 25, 100, 50), 0, GREEN)
            startButton.draw()

        case "PlayerChoose":
            screen.fill(WHITE)
            turtle_info.show(Screen=screen)
            
        case "EndScreen":
            screen.fill(WHITE)
            

        #commented because of run error
        # case _:
        #     #default
        #     pass

        case "BirdLevel":
            current_player = bird
            screen.fill(SKYBLUE)
            
            current_time = pygame.time.get_ticks()

            #Set up backround
            if current_time > end_time_cloud_animation:
                cloud_img = pygame.image.load(random.choice(cloud_img_list))
                cloud = ObstacleClass(1000, random.randint(150, 450), random.randint(5, 15), cloud_img, cloud_img.get_width(), cloud_img.get_height(), True)
                end_time_cloud_animation = pygame.time.get_ticks() + 300
                obstacle_list.append(cloud)

            for obstacle in obstacle_list:
                obstacle.move()
                

            if current_time > end_time_player_animation:
                bird.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
            screen.blit(bird.current_frame, bird.Rect)

        case "TurtleLevel":
            current_player = turtle
            screen.fill(OCEANBLUE)
            
            current_time = pygame.time.get_ticks()

            #Set up backround 
            # if current_time > end_time_cloud_animation:
            #     cloud_img = pygame.image.load(random.choice(cloud_img_list))
            #     cloud = ObstacleClass(1000, random.randint(150, 450), random.randint(5, 15), cloud_img, cloud_img.get_width(), cloud_img.get_height(), True)
            #     end_time_cloud_animation = pygame.time.get_ticks() + 300
            #     obstacle_list.append(cloud)

            # for obstacle in obstacle_list:
            #     obstacle.move()
                

            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50


            #Blit all the objects
            # for obstacle in obstacle_list:
            #     obstacle.move()
            #     if obstacle.xcor < -200:
            #         del obstacle
            #     else:
            #         screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
            screen.blit(current_player.current_frame, current_player.Rect)



    
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