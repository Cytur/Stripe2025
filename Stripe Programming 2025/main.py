import pygame
import random
from birdturtle import BirdTurtle
from ObstacleClass import ObstacleClass
from InfoCard import InfoCard
from UIClasses import TextClass, ButtonClass
from deer import Deer

# constants
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

PoppinsFont = "Poppins-Medium.ttf"
buttonlist = []
        
def CreateButton():
    pass

def changegamestate(gamestate):
     global GameState
     global buttonlist

     GameState=gamestate
     buttonlist = []

pygame.init()
pygame.display.set_caption("Animal Journey")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




#Animal Frame Lists
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

# for num in range([NUMBER_OF_FRAMES]):
#             frame = pygame.image.load(f"FRAME FILE LOCATION, WITH A WAY TO DIFFERENCIATE FILE")
#             frame = pygame.transform.scale(frame, size= (96, 96))
#             frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
#             turt_frames.append(frame)



#Animal Obj s
bird = BirdTurtle(50, 50, bird_frames)
turtle = BirdTurtle(50, 50, turt_frames)
deer = Deer(50, 400)
# deer = Deer(x, y)


#Info Cards
bird_info = InfoCard(TextClass, ButtonClass, "Red Winged Blackbird", "A stocky, red and black bird, and one", "that is very common in North America.",
                     " Air pollution, Hawks, Eagles", SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, bird_frames[0], SKYBLUE, 0, screen, changegamestate, "BirdLevel")

turtle_info = InfoCard(TextClass, ButtonClass, "Leather-Back Sea Turtle", "The largest sea turtle in the world, one", "that travels thousands of kilometers",
                       "Pollution, Sharks, Orcas", SCREEN_WIDTH_CENTER - 300, SCREEN_HEIGHT_CENTER, turt_frames[0], OCEANBLUE, 40, screen, changegamestate, "TurtleLevel")

#Obstacle Related Lists
obstacle_list = []
cloud_img_list = ["CloudAsset/Cloud 10.png", "CloudAsset/Cloud 11.png", "CloudAsset/Cloud 12.png"]



#Wait Animation Section
end_time_player_animation = 0
end_time_cloud_animation = 0
end_time_bubble_animation = 0

#Functions for Obstacles
cloud_img = pygame.image.load(random.choice(cloud_img_list))
def make_cloud(bottom_bound: int = 600):
    return ObstacleClass(1000, random.randint(0, bottom_bound), random.randint(5, 15), 0, cloud_img, cloud_img.get_width(), cloud_img.get_height(), True)

bubble_img = pygame.image.load("BubbleAsset/bubble.png")
def make_bubble():
    return ObstacleClass(random.randint(0, 840), 650,  4, random.randint(4, 5), bubble_img, bubble_img.get_width(), bubble_img.get_height(), True)





GameState = "DeerLevel"





RunVar = True
while RunVar == True:
    match GameState:
        case "TitleScreen":
            screen.fill(WHITE)
            
            titleText = TextClass("Animal Journey", pygame.font.Font(PoppinsFont, 50), BLACK, (SCREEN_WIDTH_CENTER, 175), screen)
            titleText.blit()
            
            startButton = ButtonClass(TextClass("Start", pygame.font.Font(PoppinsFont, 20), BLACK, (SCREEN_WIDTH_CENTER, 225), screen), pygame.Rect(SCREEN_WIDTH_CENTER - 50, 225 - 25, 100, 50), 0, GREEN, screen, changegamestate, "PlayerChoose")
            buttonlist.append(startButton)
            startButton.draw()




        case "PlayerChoose":
            screen.fill(WHITE)
            buttonlist.append(turtle_info.playbutton)
            buttonlist.append(bird_info.playbutton)
            turtle_info.show(Screen=screen)
            bird_info.show(Screen=screen)
            




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
                cloud = make_cloud()
                end_time_cloud_animation = pygame.time.get_ticks() + 300
                obstacle_list.append(cloud)

            for obstacle in obstacle_list:
                obstacle.move()
                

            if current_time > end_time_player_animation:
                bird.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
            screen.blit(bird.current_frame, bird.Rect)






        case "TurtleLevel":
            current_player = turtle
            screen.fill(OCEANBLUE)
            
            current_time = pygame.time.get_ticks()

            pygame.draw.rect(screen, OCEANYELLOW, pygame.Rect(0,500,840,100))


            # Set up backround 
            if current_time > end_time_bubble_animation:
                bubble = make_bubble()
                obstacle_list.append(bubble)
                end_time_bubble_animation = pygame.time.get_ticks() + random.randint(350, 450)

            for obstacle in obstacle_list:
                obstacle.move()


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
            screen.blit(current_player.current_frame, current_player.Rect)




        case "DeerLevel":
            current_player = deer

            screen.fill(SKYBLUE)
            
            current_time = pygame.time.get_ticks()

            pygame.draw.rect(screen, GRASSGREEN, pygame.Rect(0,500,840,100))


            # Set up backround 
            if current_time > end_time_cloud_animation:
                cloud = make_cloud(450)
                obstacle_list.append(cloud)
                end_time_cloud_animation = pygame.time.get_ticks() + 600

            for obstacle in obstacle_list:
                obstacle.move()


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))

            screen.blit(current_player.current_frame, current_player.Rect)





    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunVar = False

        #detecting button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            for button in buttonlist:
                if button.rectangleRender.collidepoint(mousepos):
                    button.command(button.param)
                    print("button clicked")
        
        #detecting key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            current_player.move("UP")
        if keys[pygame.K_s]:
            current_player.move("DOWN")

        #For deer
        try:
            if keys[pygame.K_SPACE]:
                current_player.jump()
        except:
            pass
            
    pygame.display.update()
    
    pygame.time.Clock().tick(60)

pygame.quit()