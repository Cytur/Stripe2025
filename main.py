import pygame
import random
import DesignClass
from birdturtle import BirdTurtle
from ObstacleClass import ObstacleClass, collide_list
from InfoCard import InfoCard
from UIClasses import TextClass, ButtonClass
from deer import Deer

buttonlist = []
        
def ChangeGameState(newGameState):
    global GameState
    global buttonlist

    GameState = newGameState
    buttonlist = []

pygame.init()
pygame.display.set_caption("Animal Journey")
screen = pygame.display.set_mode((DesignClass.SCREEN_WIDTH, DesignClass.SCREEN_HEIGHT))




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
    DesignClass.SCREEN_WIDTH_CENTER,
    DesignClass.SCREEN_HEIGHT_CENTER,
    bird_frames[0],
    DesignClass.Colors["SKYBLUE"],
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
    DesignClass.SCREEN_WIDTH_CENTER - 300,
    DesignClass.SCREEN_HEIGHT_CENTER,
    turt_frames[0],
    DesignClass.Colors["OCEANBLUE"],
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
    DesignClass.SCREEN_WIDTH_CENTER + 300,
    DesignClass.SCREEN_HEIGHT_CENTER,
    pygame.transform.scale(deer.frames[1], (28*3, 75)),
    DesignClass.Colors["GRASSGREEN"],
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
    return ObstacleClass(900, 450, 8, 0, wolf_imgs[0].get_width() * 4, wolf_imgs[0].get_height() * 4, True, wolf_imgs)



#Vars for player jumping
isJumping = False
start_acceleration = 15
vert_acceleration = 15
gravity_force = 0.7

#End screen args default
EndScreenTitle = "You Died!"
EndScreenTitleColor = DesignClass.Colors["RED"]
EndScreenReason = "N/A"
EndScreenNextStage = "TitleScreen"

def EndLevel(TitleText, TitleTextColor, EndReason, NextStage):
    global EndScreenTitle
    global EndScreenTitleColor
    global EndScreenReason
    global EndScreenNextStage
    global GameState
    
    EndScreenTitle = TitleText
    EndScreenTitleColor = TitleTextColor
    EndScreenReason = EndReason
    EndScreenNextStage = NextStage
    GameState = "EndScreen"

GameState = "TitleScreen"
RunVar = True

while RunVar == True:
    current_time = pygame.time.get_ticks()

    match GameState:
        case "TitleScreen":
            screen.fill(DesignClass.Colors["WHITE"])
            
            titleText = TextClass(
                "Animal Journey",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 50),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            titleText.blit()
            
            startButton = ButtonClass(
                TextClass(
                    "Start",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 20),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 250),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 75, 250 - 25, 150, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "PlayerChoose"
            )
            buttonlist.append(startButton)
            startButton.draw()

            controlsButton = ButtonClass(
                TextClass(
                    "Controls",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 20),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 325),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 75, 325 - 25, 150, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "ControlsPage"
            )
            controlsButton.draw()

        case "PlayerChoose":
            screen.fill(DesignClass.Colors["WHITE"])
            buttonlist.append(turtle_info.playbutton)
            buttonlist.append(bird_info.playbutton)
            buttonlist.append(deer_info.playbutton)
            turtle_info.show(Screen=screen)
            bird_info.show(Screen=screen)
            deer_info.show(Screen=screen)

        case "BirdLevel":
            current_player = bird
            screen.fill(DesignClass.Colors["SKYBLUE"])
            
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
            screen.fill(DesignClass.Colors["OCEANBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["OCEANYELLOW"], pygame.Rect(0,500,840,100))

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

            screen.fill(DesignClass.Colors["SKYBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["GRASSGREEN"], pygame.Rect(0,500,840,100))


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

            #Jumping
            if isJumping == True:
                deer.current_frame = deer.frames[4]
                
                if vert_acceleration > (-start_acceleration):
                    vert_acceleration -= gravity_force
                else:
                    isJumping = False
                    vert_acceleration = start_acceleration
                    
                current_player.jump(vert_acceleration)

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
                    
                    pygame.time.delay(1500)
                    EndLevel("You Died!", DesignClass.Colors["RED"], "Eaten by wolf", "TitleScreen")


        case "EndScreen":
            screen.fill(DesignClass.Colors["WHITE"])
            obstacle_list = []
            collide_list = []
            
            endTitle = TextClass(
                EndScreenTitle,
                pygame.font.Font(DesignClass.Fonts["Poppins"], 100),
                EndScreenTitleColor,
                (DesignClass.SCREEN_WIDTH_CENTER, 150),
                screen
            )
            endTitle.blit()
            
            endReasonText = TextClass(
                EndScreenReason,
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 250),
                screen
            )
            endReasonText.blit()
            
            continueText = TextClass(
                "Press [Space] To Continue",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 35),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 450),
                screen
            )
            continueText.blit()
            


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
                if current_player.ycor > 10:
                    current_player.move("UP")
            if keys[pygame.K_s]:
                if current_player.ycor < 500:
                    current_player.move("DOWN")
        except:
            pass
        
        #For deer
        try:
            if keys[pygame.K_SPACE]:
                if GameState == "EndScreen":
                    GameState = EndScreenNextStage
                elif GameState == "DeerLevel":
                    isJumping = True
                    print("jumped")
        except:
            pass
            
    pygame.display.update()
    
    pygame.time.Clock().tick(60)

pygame.quit()