import pygame
import random
import DesignClass
from birdturtle import BirdTurtle
from ObstacleClass import ObstacleClass, collide_list
from InfoCard import InfoCard
from UIClasses import TextClass, ButtonClass
from deer import Deer
from livesclass import Lives

buttonlist = []
km_count = 0

        
def ChangeGameState(newGameState):
    global GameState
    global buttonlist
    global end_time_text
    global km_count

    GameState = newGameState
    buttonlist = []
    end_time_text = current_time + 10000
    birdNPC.xcor = -100
    km_count = 0

def ResetGame():
    global GameState, buttonlist, end_time_text, km_count
    global obstacle_list, collide_list
    global end_time_cloud_spawn, end_time_bubble_spawn, end_time_wolf_spawn, end_time_wolf_animation, time_pass, end_time_hawk_animation, end_time_hawk_spawn, end_time_bullet_spawn
    global end_time_tree_spawn, end_time_snow_spawn, end_time_player_animation, end_time_rain_spawn
    global end_time_bNPC_move, end_time_km_update
    global isJumping, vert_acceleration
    global current_player

    buttonlist = []
    end_time_text = pygame.time.get_ticks() + 10000
    birdNPC.xcor = -100
    km_count = 0

    # reset objects
    obstacle_list = []
    collide_list = []

    # Reset all timers
    end_time_player_animation = 0
    end_time_cloud_spawn = 0
    end_time_bubble_spawn = 0
    end_time_wolf_spawn = 1000
    end_time_wolf_animation = 0
    end_time_tree_spawn = 1000
    end_time_text = 0
    end_time_snow_spawn = 0
    end_time_bNPC_move = 0
    end_time_km_update = 0
    end_time_rain_spawn = 0
    time_pass = 0
    end_time_hawk_spawn = 0
    end_time_hawk_animation = 0
    end_time_bullet_spawn = 0

    # Reset jump variables
    isJumping = False
    vert_acceleration = start_acceleration
    deer.ycor = 400

    #Reset hearts
    lives.lives = []
    
    GameState = "TitleScreen"

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
bird = BirdTurtle(50, 50, bird_frames, 64)
birdNPC = BirdTurtle(-100, 300, bird_frames, 64)
turtle = BirdTurtle(50, 400, turt_frames, 96)
deer = Deer(50, 400)
lives = Lives()


#Info Cards
bird_info = InfoCard(
    "Red Winged Blackbird",
    "A stocky, red and black bird, and one",
    "that is very common in North America.",
    " Air pollution, Hawks, Eagles",
    "Migrate in flocks",
    "13000 km from Idaho to Florida",
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
    "Long distance migration",
    "4000 km across the Atlantic",
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
    "Migrate during season change",
    "250 km across Brazil's plateaus",
    DesignClass.SCREEN_WIDTH_CENTER + 300,
    DesignClass.SCREEN_HEIGHT_CENTER,
    pygame.transform.scale(deer.icon, (28*3, 75)),
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
end_time_wolf_spawn = 1000
end_time_wolf_animation = 0
end_time_tree_spawn = 1000
end_time_text = 8000
end_time_snow_spawn = 0
end_time_bNPC_move = 0
end_time_tNPC_move = 0
end_time_km_update = 0
end_time_rain_spawn = 0
time_pass = 0
end_time_hawk_spawn = 0
end_time_hawk_animation = 0
end_time_bullet_spawn = 5000
end_time_eggs_move = 5000
end_time_trash_spawn = 5000
end_time_shark_spawn = 8000
end_time_killerwhale_spawn = 8000
end_time_hunter = 0


#Functions for Obstacles
bubble_img = pygame.image.load("BubbleAsset/bubble.png")
wolf_imgs = [pygame.image.load(f"WolfAsset/wolf{x+1}.png") for x in range(6)]
tree_img = pygame.transform.scale2x(pygame.image.load("TreeAsset/tree.png"))
snow_img = pygame.transform.scale(pygame.image.load("SnowflakeAsset/snowflakes.png"), (2, 2))
rain_img = pygame.transform.scale(pygame.image.load("RainAsset/Raindrop.png"), (10, 10))
hawk_imgs = [pygame.image.load(f"HawkAsset/bird{x+1}.png") for x in range(3)]
shark_img = pygame.transform.scale(pygame.image.load("SharkAsset/shark.png"), (32, 18))
killerwhale_img = pygame.transform.scale(pygame.image.load("KillerWhaleAsset/killerwhale.png"), (32, 18))
trash_img = pygame.transform.scale(pygame.image.load("TrashAsset/Trash.png"), (20, 18))
bottle_img = pygame.transform.scale(pygame.image.load("TrashAsset/PlasticBottle.png"), (10, 30))
bullet_img = pygame.image.load("BulletAsset/Snipe1.png")
fish_img = pygame.transform.scale(pygame.image.load("GoldfishAsset/goldfish.png"), (50, 35))
hunter_imgs = [pygame.image.load(f"HunterAsset/hunter{x+1}.png") for x in range(6)]
#wolf_imgs = [pygame.image.load("white.png")]

def make_cloud(bottom_bound: int = 600):
    cloud_img = pygame.image.load(random.choice(cloud_img_list))
    return ObstacleClass(1000, random.randint(0, bottom_bound), random.randint(5, 15), 0, cloud_img.get_width()/2, cloud_img.get_height()/2, False, [cloud_img], "Cloud")

def make_bubble():
    return ObstacleClass(random.randint(0, 840), 650,  4, random.randint(4, 5), bubble_img.get_width(), bubble_img.get_height(), False, [bubble_img], "Bubble")

def make_wolf():
    return ObstacleClass(900, 450, 8, 0, wolf_imgs[0].get_width(), wolf_imgs[0].get_height(), True, wolf_imgs, "Wolf")

def make_tree():
    return ObstacleClass(1000, random.randint(0, 500), 10, 0, 16, tree_img.get_height(), True, [tree_img], "Tree")

def make_snow():
    return ObstacleClass(random.randint(0, 1680), -5, 20, -20, 3, 3, False, [snow_img], "Snow")

def make_rain_diagonal():
    return ObstacleClass(random.randint(0, 1680), -5, 20, -20, 3, 3, False, [rain_img], "Rain")

def make_rain_straight():
    return ObstacleClass(random.randint(0, 1680), -5, 0, -20, 3, 3, False, [rain_img], "Rain")

def make_hawk():
    return ObstacleClass(1000, current_player.ycor, 20, random.randint(-2, 2), hawk_imgs[0].get_width(), hawk_imgs[0].get_height(), True, hawk_imgs, "Hawk")
    
def make_bullet():
    return ObstacleClass(current_player.xcor, -40, 0, -7, bullet_img.get_width()/2, bullet_img.get_height()/2,True, [bullet_img], "Hunter")

def make_shark():
    return ObstacleClass(1000, random.randint(0, 400), 5, 0, shark_img.get_width(), shark_img.get_height(), True, [shark_img], "Shark")

def make_killerwhale():
    return ObstacleClass(1000, random.randint(0, 400), 5, 0, killerwhale_img.get_width(), killerwhale_img.get_height(), True, [killerwhale_img], "Killer Whale")

def make_trash():
    return ObstacleClass(1000, random.randint(0, 400), 3, 0, trash_img.get_width(), trash_img.get_height(), True, [trash_img], "Trash")

def make_bottle():
    return ObstacleClass(1000, random.randint(0, 400), 3, 0, bottle_img.get_width(), bottle_img.get_height(), True, [bottle_img], "Plastic bottle")
    
fishNPC = BirdTurtle(1000, 150, [fish_img], 10)

def make_hunter():
    return ObstacleClass(-180, 450, -10, 0, hunter_imgs[0].get_width(), hunter_imgs[0].get_height(), True, hunter_imgs, "Wolf")


#Vars for player jumping
isJumping = False
start_acceleration = 12
vert_acceleration = 12
gravity_force = 0.5

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
    global km_count
    global GameState
    
    EndScreenTitle = TitleText
    EndScreenTitleColor = TitleTextColor
    EndScreenReason = EndReason
    EndScreenNextStage = NextStage
    km_count = 0
    GameState = "EndScreen"

GameState = "Deer Level 2"
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
            buttonlist.append(controlsButton)
            controlsButton.draw()

        case "PlayerChoose":
            screen.fill(DesignClass.Colors["WHITE"])

            titleText = TextClass(
                "Animal Journey",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 50),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 75),
                screen
            )
            titleText.blit()

            buttonlist.append(turtle_info.playbutton)
            buttonlist.append(bird_info.playbutton)
            buttonlist.append(deer_info.playbutton)
            turtle_info.show(Screen=screen)
            bird_info.show(Screen=screen)
            deer_info.show(Screen=screen)

        case "BirdLevel":
            current_player = bird
            routelen = 6000
            lives.load_hearts(2)
            screen.fill(DesignClass.Colors["FORESTGREEN"])

            instructText = TextClass(
                "Hurry Up! Pass through tree trunks",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )
            
            
            
            #Set up backround
            if current_time > end_time_tree_spawn:
                tree = make_tree()
                end_time_tree_spawn = pygame.time.get_ticks() + 1000
                obstacle_list.append(tree)
                collide_list.append(tree)

            if current_time > end_time_snow_spawn:
                snow = make_snow()
                end_time_snow_spawn = pygame.time.get_ticks() + 40
                obstacle_list.append(snow)

            if current_time > end_time_bNPC_move:
                birdNPC.move("RIGHT")
                end_time_bNPC_move += 80

            if current_time > end_time_km_update:
                km_count += 3
                end_time_km_update = pygame.time.get_ticks() + 1

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Level Won", "Bird Level 2")

            for obstacle in obstacle_list:
                obstacle.move()

            
                

            if current_time > end_time_player_animation:
                birdNPC.animation_update()
                bird.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    obstacle_list.remove(obstacle)
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], obstacle.Rect)

            if birdNPC.xcor < 1000:
                screen.blit(birdNPC.current_frame, birdNPC.Rect)

            screen.blit(bird.current_frame, bird.Rect)
            # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], bird.Rect)d

            for heart in lives.lives:
                img = heart[0]
                rect = heart[1]
                screen.blit(img, rect)

            if current_time < end_time_text:
                instructText.blit()
            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    dead = lives.remove_life()
                    print(obstacle.xcor, obstacle.ycor)
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")


        case "TurtleLevel":
            current_player = turtle
            routelen = 2000
            lives.load_hearts(2)

            screen.fill(DesignClass.Colors["OCEANBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["OCEANYELLOW"], pygame.Rect(0,500,840,100))

            eggs = pygame.transform.scale(pygame.image.load("TurtleExtraAsset/cracked-egg.png"), (86, 56))

            instructText = TextClass(
                "Embark on your journey, avoid trash and sharks!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )

            # Set up backround 
            if current_time > end_time_bubble_spawn:
                bubble = make_bubble()
                obstacle_list.append(bubble)
                end_time_bubble_spawn = pygame.time.get_ticks() + random.randint(350, 450)

            if current_time > end_time_trash_spawn:
                trash = make_trash()
                obstacle_list.append(trash)
                end_time_trash_spawn = pygame.time.get_ticks() + 7000
                obstacle_list.append(trash)
                collide_list.append(trash)

            if current_time > end_time_shark_spawn:
                shark = make_shark()
                obstacle_list.append(shark)
                end_time_shark_spawn = pygame.time.get_ticks() + random.randint(3000,8000)
                obstacle_list.append(shark)
                collide_list.append(shark)

            if current_time < end_time_eggs_move:
                screen.blit(eggs, eggs.get_rect(center=(50,500)))

            for obstacle in obstacle_list:
                obstacle.move()

            if km_count < 300:
                instructText.blit()

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Level Won", "Turtle Level 2")

            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 1


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))

            screen.blit(current_player.current_frame, current_player.Rect)

            for heart in lives.lives:
                img = heart[0]
                rect = heart[1]
                screen.blit(img, rect)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")

        case "Turtle Level 2":
            current_player = turtle
            routelen = 2000
            lives.load_hearts(2)

            screen.fill(DesignClass.Colors["OCEANBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["OCEANYELLOW"], pygame.Rect(0,500,840,100))

            instructText = TextClass(
                "Get to the end and lay your eggs! Beware: Killer Sharks",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )

            # Set up backround 
            if current_time > end_time_bubble_spawn:
                bubble = make_bubble()
                obstacle_list.append(bubble)
                end_time_bubble_spawn = pygame.time.get_ticks() + random.randint(350, 450)

            if current_time > end_time_tNPC_move:
                fishNPC.move("LEFT")
                end_time_tNPC_move += 80

            if current_time > end_time_trash_spawn:
                bottle = make_bottle()
                obstacle_list.append(bottle)
                end_time_trash_spawn = pygame.time.get_ticks() + 7000
                obstacle_list.append(bottle)
                collide_list.append(bottle)

            if current_time > end_time_killerwhale_spawn:
                killerwhale = make_killerwhale()
                obstacle_list.append(killerwhale)
                end_time_killerwhale_spawn = pygame.time.get_ticks() + random.randint(3000,8000)
                obstacle_list.append(killerwhale)
                collide_list.append(killerwhale)

            if km_count < 200:
                instructText.blit()

            if km_count > routelen:
                EndLevel("You Won!", DesignClass.Colors["GREEN"], "Congratulations, try other animals!", "TitleScreen")

            for obstacle in obstacle_list:
                obstacle.move()


            if current_time > end_time_player_animation:
                fishNPC.animation_update()
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 1


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
            
            if fishNPC.xcor < 1000:
                screen.blit(fishNPC.current_frame, fishNPC.Rect)

            screen.blit(current_player.current_frame, current_player.Rect)

            for heart in lives.lives:
                img = heart[0]
                rect = heart[1]
                screen.blit(img, rect)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")


        case "DeerLevel":
            current_player = deer
            deer.xcor = 50
            routelen = 250
            lives.load_hearts(2)
            time_pass += 1

            screen.fill(DesignClass.Colors["SKYBLUE"])

            pygame.draw.rect(screen, DesignClass.Colors["GRASSGREEN"], pygame.Rect(0,500,840,100))

            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )

            # Set up backround 
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud(300)
                obstacle_list.append(cloud)
                end_time_cloud_spawn = pygame.time.get_ticks() + 600

            if current_time > end_time_wolf_spawn:
                wolf = make_wolf()
                print("wolf spawned")
                obstacle_list.append(wolf)
                collide_list.append(wolf)
                end_time_wolf_spawn = pygame.time.get_ticks() + 7000 #random.randint(7000,21000)

            if current_time > end_time_rain_spawn:
                rain = make_rain_diagonal()
                end_time_rain_spawn = pygame.time.get_ticks() + 15
                obstacle_list.append(rain)

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 200

            for obstacle in obstacle_list:
                obstacle.update_frame()
                obstacle.move()


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Level Won", "Deer Level 2")

            #Jumping
            if isJumping == True:
                deer.current_frame = deer.frames[4]

                current_player.jump(vert_acceleration)
                
                if vert_acceleration > (-start_acceleration):
                    vert_acceleration -= gravity_force
                else:
                    isJumping = False
                    vert_acceleration = start_acceleration

            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    

            screen.blit(current_player.current_frame, current_player.Rect)

            for heart in lives.lives:
                img = heart[0]
                rect = heart[1]
                screen.blit(img, rect)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")

        case "Bird Level 2":
            current_player = bird
            routelen = 7000
            lives.load_hearts(2)
            screen.fill(DesignClass.Colors["SKYBLUE"])

            instructText = TextClass(
                "You're catching up! Watch out for eagles!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count}km",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (100, 25),
                screen
            )
            
            
            
            #Set up backround
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud()
                end_time_cloud_spawn = pygame.time.get_ticks() + 700
                obstacle_list.append(cloud)


            if current_time > end_time_snow_spawn:
                snow = make_snow()
                end_time_snow_spawn = pygame.time.get_ticks() + 60 + time_pass/180
                obstacle_list.append(snow)

            if current_time > end_time_hawk_spawn:
                hawk = make_hawk()
                end_time_hawk_spawn = pygame.time.get_ticks() + 800
                obstacle_list.append(hawk)
                collide_list.append(hawk)

            if current_time > end_time_bNPC_move:
                birdNPC.move("RIGHT")
                end_time_bNPC_move += 80

            if current_time > end_time_km_update:
                km_count += 3
                end_time_km_update += 1

            if km_count > routelen:
                EndLevel("You Won, Try Other Animals Too!", DesignClass.Colors["GREEN"], "Level Won", "TitleScreen")

            for obstacle in obstacle_list:
                obstacle.move()
                obstacle.update_frame()


            if current_time > end_time_player_animation:
                birdNPC.animation_update()
                bird.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 50


            #Blit all the objects
            for obstacle in obstacle_list:
                if obstacle.xcor < -200:
                    obstacle_list.remove(obstacle)
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], obstacle.Rect)

            if birdNPC.xcor < 1000:
                screen.blit(birdNPC.current_frame, birdNPC.Rect)

            screen.blit(bird.current_frame, bird.Rect)
            # pygame.draw.rect(screen, DesignClass.Colors["GREEN"], bird.Rect)d

            for heart in lives.lives:
                img = heart[0]
                rect = heart[1]
                screen.blit(img, rect)

            if current_time < end_time_text:
                instructText.blit()
            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    dead = lives.remove_life()
                    print(obstacle.xcor, obstacle.ycor)
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")

        case "Deer Level 2":
            current_player = deer
            routelen = 24
            lives.load_hearts(3)
            time_pass += 1

            screen.fill([170,206,250])

            pygame.draw.rect(screen, DesignClass.Colors["GRASSGREEN"], pygame.Rect(0,500,840,100))

            instructText = TextClass(
                "Dodge the bullets! The hunters have found you!",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (DesignClass.SCREEN_WIDTH_CENTER, 125),
                screen
            )
            kmText = TextClass(
                f"{km_count} hours till safe",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 40),
                DesignClass.Colors["BLACK"],
                (200, 25),
                screen
            )

            # Set up backround 
            if current_time > end_time_cloud_spawn:
                cloud = make_cloud(300)
                obstacle_list.append(cloud)
                end_time_cloud_spawn = pygame.time.get_ticks() + 600

            if current_time > end_time_rain_spawn:
                rain = make_rain_straight()
                end_time_rain_spawn = pygame.time.get_ticks() + 15
                obstacle_list.append(rain)

            if current_time > end_time_bullet_spawn:
                if end_time_bullet_spawn == 0:
                    end_time_bullet_spawn = pygame.time.get_ticks() + 5000
                    pass
                bullet = make_bullet()
                end_time_bullet_spawn = pygame.time.get_ticks() + 1300
                obstacle_list.append(bullet)
                collide_list.append(bullet)

            if current_time > end_time_hunter:
                hunter = make_hunter()
                obstacle_list.append(hunter)
                end_time_hunter = 2222222
            

            if current_time > end_time_km_update:
                km_count += 1
                end_time_km_update += 5000

            for obstacle in obstacle_list:
                obstacle.update_frame()
                obstacle.move()


            if current_time > end_time_player_animation:
                current_player.animation_update()
                end_time_player_animation = pygame.time.get_ticks() + 60

            if km_count > routelen:
                EndLevel("You Won", DesignClass.Colors["GREEN"], "Level Won", "TitleScreen")


            #Blit all the objects
            for obstacle in obstacle_list:
                obstacle.move()
                if obstacle.xcor < -200:
                    del obstacle
                else:
                    screen.blit(obstacle.image, (obstacle.xcor, obstacle.ycor))
                    
            deer.blit(screen)
            screen.blit(current_player.current_frame, current_player.Rect)

            if current_time < end_time_text:
                instructText.blit()
                end_time_text += 10000

            for heart in lives.lives:
                img = heart[0]
                rect = heart[1]
                screen.blit(img, rect)

            kmText.blit()

            #detecting player collisions with objects
            for obstacle in collide_list:
                if current_player.Rect.colliderect(obstacle.Rect):
                    dead = lives.remove_life()
                    pygame.time.delay(100)
                    collide_list.remove(obstacle)
                    if dead:
                        EndLevel("You died!", DesignClass.Colors["RED"], "Unfortunately, you did not migrate successfully.", "TitleScreen")



        
        case "ControlsPage":
            screen.fill(DesignClass.Colors["WHITE"])

            UpDownText = TextClass(
                "Up/Down (Bird & Turtle)",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (330, 50),
                screen
            )
            UpDownText.blit()
            Key_W = pygame.transform.scale(pygame.image.load("KeyboardAsset/W.png"), (40,40))
            screen.blit(Key_W, Key_W.get_rect(center = (50, 50)))
            Key_S = pygame.transform.scale(pygame.image.load("KeyboardAsset/S.png"), (40,40))
            screen.blit(Key_S, Key_S.get_rect(center = (95, 50)))

            JumpText = TextClass(
                "Jump (Deer)",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (250, 150),
                screen
            )
            JumpText.blit()
            Key_Space = pygame.transform.scale(pygame.image.load("KeyboardAsset/SPACE.png"), (100,40))
            screen.blit(Key_Space, Key_Space.get_rect(center = (80, 150)))

            EscText = TextClass(
                "Shortcut to main menu",
                pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                DesignClass.Colors["BLACK"],
                (270, 240),
                screen
            )
            EscText.blit()
            Key_Esc = pygame.transform.scale(pygame.image.load("KeyboardAsset/ESC.png"), (40,40))
            screen.blit(Key_Esc, Key_Esc.get_rect(center = (50, 240)))

            BackButton = ButtonClass(
                TextClass(
                    "Understood!",
                    pygame.font.Font(DesignClass.Fonts["Poppins"], 30),
                    DesignClass.Colors["BLACK"],
                    (DesignClass.SCREEN_WIDTH_CENTER, 500),
                    screen
                ),
                pygame.Rect(DesignClass.SCREEN_WIDTH_CENTER - 175, 475, 350, 50),
                0,
                DesignClass.Colors["GREEN"],
                screen,
                ChangeGameState,
                "TitleScreen"
            )
            buttonlist.append(BackButton)
            BackButton.draw()
            


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
                    #print("button clicked")

        #Detecting key presses
        keys = pygame.key.get_pressed()
        try:
            if keys[pygame.K_w]:
                #Height limit
                if current_player.ycor > 10:
                    current_player.move("UP")
            if keys[pygame.K_s]:
                if current_player.ycor < 500:
                    current_player.move("DOWN")

            if GameState == "Deer Level 2":
                if keys[pygame.K_d]:
                    if current_player.xcor < 730:
                      
                        current_player.move("RIGHT")

                if keys[pygame.K_a]:
                  
                    if current_player.ycor > 15:
                        current_player.move("LEFT")
        except:
            pass
        
        #For deer
        try:
            if keys[pygame.K_SPACE]:
                if GameState == "EndScreen":
                    pygame.time.delay(100)
                    GameState = EndScreenNextStage
                elif GameState == "DeerLevel":
                    isJumping = True
 
        except:
            pass

        #Returning to main menu during gameplay
        try:
            if keys[pygame.K_ESCAPE]:
                ResetGame()
        except:
            pass
            
    pygame.display.update()
    
    pygame.time.Clock().tick(40)

pygame.quit()