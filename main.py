import pygame
import random
from birdturtle import BirdTurtle
from ObstacleClass import ObstacleClass, collide_list
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

def ChangeGameState(newGameState):
    global GameState
    global buttonlist

    GameState = newGameState
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
#    frame = pygame.image.load(f"FRAME FILE LOCATION, WITH A WAY TO DIFFERENCIATE FILE")
#    frame = pygame.transform.scale(frame, size= (96, 96))
#    frame = pygame.transform.flip(frame, flip_x=True, flip_y=False)
#    turt_frames.append(frame)



#Animal Obj s
bird = BirdTurtle(50, 50, bird_frames)
turtle = BirdTurtle(50, 50, turt_frames)
deer = Deer(50, 400)
# deer = Deer(x, y)


#Info Cards
bird_info = InfoCard(
    "Red Winged Blackbird",
    "A stocky, red and black bird, and one",
    "that is very common in North America.",
    " Air pollution, Hawks, Eagles",
    SCREEN_WIDTH_CENTER,
    SCREEN_HEIGHT_CENTER,
    bird_frames[0],
    SKYBLUE,
    0,
    screen,
    ChangeGameState,
    "BirdLevel"
)

turtle_info = InfoCard(
    "Leather-Back Sea Turtle",
    "The largest sea turtle in the world, one",
    "that travels thousands of kilometers",
    "Pollution, Sharks",
    SCREEN_WIDTH_CENTER - 300,
    SCREEN_HEIGHT_CENTER,
    turt_frames[0],
    OCEANBLUE,
    40,
    screen,
    ChangeGameState,
    "TurtleLevel"
)

deer_info = InfoCard(
    "White-Tailed Deer",
    "A white and brown deer, which is",
    "abundant all over Central America",
    "Wolves, Habitat Loss",
    SCREEN_WIDTH_CENTER + 300,
    SCREEN_HEIGHT_CENTER,
    pygame.transform.scale(deer.frames[1], (28*3, 75)),
    GRASSGREEN,
    40,
    screen,
    ChangeGameState,
    "DeerLevel"
)

#Obstacle Related Lists
obstacle_list = []
cloud_img_list = ["CloudAsset/Cloud 10.png", "CloudAsset/Cloud 11.png", "CloudAsset/Cloud 12.png"]



#Wait Animation Section
end_time_player_animation = 0
end_time_cloud_spawn = 0
end_time_bubble_spawn = 0
end_time_wolf_spawn = 0
end_time_wolf_animation = 0

#Functions for Obstacles
cloud_img = pygame.image.load(random.choice(cloud_img_list))
bubble_img = pygame.image.load("BubbleAsset/bubble.png")
wolf_imgs = [pygame.image.load(f"WolfAsset/wolf{x+1}.png") for x in range(6)]

def make_cloud(bottom_bound: int = 600):
    return ObstacleClass(1000, random.randint(0, bottom_bound), random.randint(5, 15), 0, cloud_img.get_width(), cloud_img.get_height(), False, [cloud_img])

def make_bubble():
    return ObstacleClass(random.randint(0, 840), 650,  4, random.randint(4, 5), bubble_img.get_width(), bubble_img.get_height(), False, [bubble_img])

def make_wolf():
    return ObstacleClass(900, 450,  8, 0, wolf_imgs[0].get_width() * 4, wolf_imgs[0].get_height() * 4, True, wolf_imgs)




GameState = "TitleScreen"
RunVar = True

while RunVar == True:
    match GameState:
        case "TitleScreen":
            screen.fill(WHITE)
            
            titleText = TextClass("Animal Journey", pygame.font.Font(PoppinsFont, 50), BLACK, (SCREEN_WIDTH_CENTER, 175), screen)
            titleText.blit()
            
            startButton = ButtonClass(TextClass("Start", pygame.font.Font(PoppinsFont, 20), BLACK, (SCREEN_WIDTH_CENTER, 225), screen), pygame.Rect(SCREEN_WIDTH_CENTER - 50, 225 - 25, 100, 50), 0, GREEN, screen, ChangeGameState, "PlayerChoose")
            buttonlist.append(startButton)
            startButton.draw()

        case "PlayerChoose":
            screen.fill(WHITE)
            buttonlist.append(turtle_info.playbutton)
            buttonlist.append(bird_info.playbutton)
            buttonlist.append(deer_info.playbutton)
            turtle_info.show(Screen=screen)
            bird_info.show(Screen=screen)
            deer_info.show(Screen=screen)

        case "BirdLevel":
            current_player = bird
            screen.fill(SKYBLUE)
            
            current_time = pygame.time.get_ticks()

            #Set up backround
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud()
                end_time_cloud_spawn = pygame.time.get_ticks() + 300
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


            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    ChangeGameState("EndScreen")


        case "TurtleLevel":
            current_player = turtle
            screen.fill(OCEANBLUE)
            
            current_time = pygame.time.get_ticks()

            pygame.draw.rect(screen, OCEANYELLOW, pygame.Rect(0,500,840,100))


            # Set up backround 
            if current_time > end_time_bubble_spawn:
                bubble = make_bubble()
                obstacle_list.append(bubble)
                end_time_bubble_spawn = pygame.time.get_ticks() + random.randint(350, 450)

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

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    ChangeGameState("EndScreen")


        case "DeerLevel":
            current_player = deer

            screen.fill(SKYBLUE)
            
            current_time = pygame.time.get_ticks()

            pygame.draw.rect(screen, GRASSGREEN, pygame.Rect(0,500,840,100))


            # Set up backround 
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud(450)
                obstacle_list.append(cloud)
                end_time_cloud_spawn = pygame.time.get_ticks() + 600

            if current_time > end_time_wolf_spawn:
                wolf = make_wolf()
                print("wolf spawned")
                obstacle_list.append(wolf)
                end_time_wolf_spawn = pygame.time.get_ticks() + 4000

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

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    print(obstacle.xcor)
                    
                    pygame.time.delay(4000)
                    ChangeGameState("EndScreen")


        case "EndScreen":
            screen.fill(WHITE)
            obstacle_list = []


        #Commented because of run error
        # case _:
        #     #default
        #     pass


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RunVar = False

        #Detecting button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            for button in buttonlist:
                if button.rectangleRender.collidepoint(mousepos):
                    button.command(button.param)
                    print("button clicked")

        #Detecting key presses
        keys = pygame.key.get_pressed()
        try:
            if keys[pygame.K_w]:
                current_player.move("UP")
            if keys[pygame.K_s]:
                current_player.move("DOWN")
        except:
            pass
        
        #For deer
        try:
            if keys[pygame.K_SPACE]:
                current_player.jump()
        except:
            pass
            
    pygame.display.update()
    
    pygame.time.Clock().tick(60)

pygame.quit()